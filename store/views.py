from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    search = request.GET.get('search', '').strip()
    category = request.GET.get('category', '').strip()

    products = Product.objects.all()

    # Search by product name
    if search:
        products = products.filter(name__icontains=search)

    # Category filtering
    if category == 'Electronics':
        products = products.filter(
            category__in=[
                'Electronics',
                'Laptops'
            ]
        )

    elif category == 'Fashion':
        products = products.filter(category='Fashion')

    elif category == 'Home':
        products = products.filter(category='Home')

    elif category == 'Beauty':
        products = products.filter(category='Beauty')

    elif category == 'Footwear':
        products = products.filter(
            category__in=[
                'Footwear',
                'Shoes'
            ]
        )

    elif category == 'Kids':
        products = products.filter(category='Kids')

    elif category == 'Gaming':
        products = products.filter(category='Gaming')

    elif category == 'Laptops':
        products = products.filter(category='Laptops')

    elif category == 'Shoes':
        products = products.filter(category='Shoes')

    categories = Product.objects.values_list(
        'category',
        flat=True
    ).distinct()

    return render(request, 'home.html', {
        'products': products,
        'search': search,
        'category': category,
        'categories': categories,
    })
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'product_detail.html', {
        'product': product
    })


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    product = Product.objects.get(id=product_id)
    product_id = str(product_id)

    current_quantity = cart.get(product_id, 0)

    if current_quantity < product.stock:
        cart[product_id] = current_quantity + 1
    else:
        return redirect('cart')

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def cart(request):
    cart = request.session.get('cart', {})

    cart_items = []

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))

            cart_items.append({
                 'product': product,
                 'quantity': quantity,
                 'total': product.price * quantity,
})

        except Product.DoesNotExist:
            continue 

    grand_total = sum(item['total'] for item in cart_items)     

    return render(request, 'cart.html', {
    'cart_items': cart_items,
    'grand_total': grand_total,
})
def update_cart(request, product_id, action):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        product = Product.objects.get(id=int(product_id))

        if action == 'increase':
            if cart[product_id] < product.stock:
                cart[product_id] += 1

        elif action == 'decrease':
            cart[product_id] -= 1

            if cart[product_id] <= 0:
                del cart[product_id]

        elif action == 'remove':
            del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')
def checkout(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart = request.session.get('cart', {})
    cart_items = []

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total': product.price * quantity,
            })

        except Product.DoesNotExist:
            continue

    grand_total = sum(item['total'] for item in cart_items)

    if not cart_items:
        return redirect('cart')

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Save customer details in session
        request.session['checkout_data'] = {
            'name': name,
            'phone': phone,
            'address': address,
        }

        # Create Order in database
        order = Order.objects.create(
            user=request.user,
            name=name,
            phone=phone,
            address=address,
            total_amount=grand_total,
            status='Placed'
        )

        # Create Order Items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['product'].price
            )

        # Remember the order for the payment page
        request.session['order_id'] = order.id
        request.session.modified = True

        # Continue to payment page
        return redirect('payment')

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'grand_total': grand_total,
    })

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'This username is already registered. Please use another username.'
            })

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('home')

def my_orders(request):
    orders = Order.objects.filter(
        user=request.user
    ).prefetch_related('items').order_by('-created_at')

    return render(request, 'my_orders.html', {
        'orders': orders
    })
def payment(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart = request.session.get('cart', {})
    cart_items = []

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total': product.price * quantity,
            })

        except Product.DoesNotExist:
            continue

    grand_total = sum(item['total'] for item in cart_items)

    # If cart is empty
    if not cart_items:
        return redirect('cart')

    if request.method == 'POST':

        # Get selected payment method
        payment_method = request.POST.get('payment_method')

        # Get checkout details saved earlier
        checkout_data = request.session.get('checkout_data', {})

        name = checkout_data.get('name')
        phone = checkout_data.get('phone')
        address = checkout_data.get('address')

        # Create order
        order = Order.objects.create(
            user=request.user,
            name=name,
            phone=phone,
            address=address,
            total_amount=grand_total,
            status='Placed'
        )

        # Create order items and reduce stock
        for item in cart_items:

            product = item['product']
            quantity = item['quantity']

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

            product.stock -= quantity
            product.save()

        # Clear cart
        request.session['cart'] = {}

        # Clear checkout information
        request.session['checkout_data'] = {}

        # Save payment method in session
        request.session['payment_method'] = payment_method
        request.session.modified = True

        # Go to success page
        return render(request, 'order_success.html', {
            'name': name,
            'phone': phone,
            'address': address,
            'grand_total': grand_total,
            'payment_method': payment_method,
        })

    return render(request, 'payment.html', {
        'cart_items': cart_items,
        'grand_total': grand_total,
    })
def my_orders(request):
    if not request.user.is_authenticated:
        return redirect('login')

    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'my_orders.html', {
        'orders': orders
    })