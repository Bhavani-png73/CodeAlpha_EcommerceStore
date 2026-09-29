from django.core.management.base import BaseCommand
from store.models import Product


class Command(BaseCommand):
    help = "Load a complete sample product catalogue automatically"

    def handle(self, *args, **kwargs):

        products = [

            # =========================
            # ELECTRONICS
            # =========================

            {
                "name": "Samsung Galaxy S25",
                "description": "Latest Samsung smartphone with powerful performance.",
                "category": "Electronics",
                "price": 79999,
                "image": "https://images.unsplash.com/photo-1598327105666-5b89351aff97",
                "stock": 10,
            },
            {
                "name": "iPhone 16 Pro",
                "description": "Premium Apple smartphone with advanced camera.",
                "category": "Electronics",
                "price": 119999,
                "image": "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd",
                "stock": 8,
            },
            {
                "name": "OnePlus 13",
                "description": "High performance Android smartphone.",
                "category": "Electronics",
                "price": 69999,
                "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9",
                "stock": 12,
            },
            {
                "name": "HP Pavilion Laptop",
                "description": "Powerful laptop suitable for students and professionals.",
                "category": "Electronics",
                "price": 65000,
                "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853",
                "stock": 10,
            },
            {
                "name": "MacBook Air",
                "description": "Lightweight Apple laptop with excellent performance.",
                "category": "Electronics",
                "price": 99999,
                "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853",
                "stock": 7,
            },
            {
                "name": "Wireless Headphones",
                "description": "Comfortable wireless headphones with clear sound.",
                "category": "Electronics",
                "price": 2499,
                "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e",
                "stock": 20,
            },
            {
                "name": "Wireless Mouse",
                "description": "Smooth wireless mouse for work and study.",
                "category": "Electronics",
                "price": 799,
                "image": "https://images.unsplash.com/photo-1527814050087-3793815479db",
                "stock": 25,
            },
            {
                "name": "Wireless Keyboard",
                "description": "Slim wireless keyboard for students and professionals.",
                "category": "Electronics",
                "price": 999,
                "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3",
                "stock": 15,
            },
            {
                "name": "Apple iPad",
                "description": "Modern tablet for entertainment, study and work.",
                "category": "Electronics",
                "price": 55000,
                "image": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0",
                "stock": 9,
            },
            {
                "name": "Smart Watch",
                "description": "Stylish smartwatch with fitness tracking features.",
                "category": "Electronics",
                "price": 3999,
                "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30",
                "stock": 18,
            },


            # =========================
            # WOMEN'S + MEN'S FASHION
            # =========================

            {
                "name": "Women's Floral Dress",
                "description": "Beautiful floral dress for casual occasions.",
                "category": "Fashion",
                "price": 1299,
                "image": "https://images.unsplash.com/photo-1595777457583-95e059d581b8",
                "stock": 20,
            },
            {
                "name": "Women's Kurti",
                "description": "Elegant ethnic kurti for everyday wear.",
                "category": "Fashion",
                "price": 899,
                "image": "https://images.unsplash.com/photo-1529139574466-a303027c1d8b",
                "stock": 25,
            },
            {
                "name": "Women's Saree",
                "description": "Traditional stylish saree suitable for special occasions.",
                "category": "Fashion",
                "price": 1799,
                "image": "https://images.unsplash.com/photo-1610030469983-98e550d6193c",
                "stock": 15,
            },
            {
                "name": "Women's Casual Top",
                "description": "Comfortable and trendy women's casual top.",
                "category": "Fashion",
                "price": 699,
                "image": "https://images.unsplash.com/photo-1525507119028-ed4c629a60a3",
                "stock": 30,
            },
            {
                "name": "Women's Jeans",
                "description": "Comfortable slim-fit jeans for women.",
                "category": "Fashion",
                "price": 1499,
                "image": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246",
                "stock": 18,
            },
            {
                "name": "Women's Handbag",
                "description": "Stylish handbag for everyday use.",
                "category": "Fashion",
                "price": 1199,
                "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3",
                "stock": 22,
            },
            {
                "name": "Men's Formal Shirt",
                "description": "Classic formal shirt for office and professional wear.",
                "category": "Fashion",
                "price": 999,
                "image": "https://images.unsplash.com/photo-1603252110481-7ba873bf42ab",
                "stock": 25,
            },
            {
                "name": "Men's T-Shirt",
                "description": "Comfortable cotton T-shirt for everyday wear.",
                "category": "Fashion",
                "price": 599,
                "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab",
                "stock": 35,
            },
            {
                "name": "Men's Jeans",
                "description": "Classic denim jeans with comfortable fitting.",
                "category": "Fashion",
                "price": 1399,
                "image": "https://images.unsplash.com/photo-1542272604-787c3835535d",
                "stock": 20,
            },
            {
                "name": "Men's Jacket",
                "description": "Modern casual jacket for outdoor and winter wear.",
                "category": "Fashion",
                "price": 2299,
                "image": "https://images.unsplash.com/photo-1551028719-00167b16eac5",
                "stock": 12,
            },


            # =========================
            # KIDS
            # =========================

            {
                "name": "Girls Party Dress",
                "description": "Cute party dress for girls.",
                "category": "Kids",
                "price": 999,
                "image": "https://images.unsplash.com/photo-1518831959646-742c3a14ebf7",
                "stock": 15,
            },
            {
                "name": "Boys T-Shirt",
                "description": "Comfortable printed T-shirt for boys.",
                "category": "Kids",
                "price": 499,
                "image": "https://images.unsplash.com/photo-1519238263530-99bdd11df2ea",
                "stock": 20,
            },
            {
                "name": "Kids School Bag",
                "description": "Colorful and durable school bag for children.",
                "category": "Kids",
                "price": 799,
                "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62",
                "stock": 18,
            },
            {
                "name": "Kids Sports Shoes",
                "description": "Comfortable sports shoes for active children.",
                "category": "Kids",
                "price": 899,
                "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff",
                "stock": 16,
            },
            {
                "name": "Kids Building Blocks",
                "description": "Colorful building blocks for creative play.",
                "category": "Kids",
                "price": 599,
                "image": "https://images.unsplash.com/photo-1596461404969-9ae70f2830c1",
                "stock": 30,
            },


            # =========================
            # BEAUTY
            # =========================

            {
                "name": "Matte Lipstick",
                "description": "Long-lasting matte lipstick with smooth finish.",
                "category": "Beauty",
                "price": 499,
                "image": "https://images.unsplash.com/photo-1586495777744-4413f21062fa",
                "stock": 30,
            },
            {
                "name": "Makeup Kit",
                "description": "Complete makeup kit for everyday styling.",
                "category": "Beauty",
                "price": 1299,
                "image": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796",
                "stock": 15,
            },
            {
                "name": "Face Wash",
                "description": "Gentle face wash for fresh and clean skin.",
                "category": "Beauty",
                "price": 349,
                "image": "https://images.unsplash.com/photo-1556229010-6c3f2c9ca5f8",
                "stock": 25,
            },
            {
                "name": "Perfume",
                "description": "Elegant fragrance suitable for everyday use.",
                "category": "Beauty",
                "price": 999,
                "image": "https://images.unsplash.com/photo-1541643600914-78b084683601",
                "stock": 20,
            },
            {
                "name": "Skin Care Set",
                "description": "Daily skincare products for a simple skincare routine.",
                "category": "Beauty",
                "price": 1499,
                "image": "https://images.unsplash.com/photo-1556228578-8c89e6adf883",
                "stock": 12,
            },


            # =========================
            # HOME
            # =========================

            {
                "name": "Cotton Bedsheet",
                "description": "Soft cotton bedsheet with modern design.",
                "category": "Home",
                "price": 999,
                "image": "https://images.unsplash.com/photo-1631049307264-da0ec9d70304",
                "stock": 20,
            },
            {
                "name": "Table Lamp",
                "description": "Modern decorative lamp for bedroom and study table.",
                "category": "Home",
                "price": 799,
                "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c",
                "stock": 15,
            },
            {
                "name": "Curtains",
                "description": "Stylish curtains for living room and bedroom.",
                "category": "Home",
                "price": 899,
                "image": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace",
                "stock": 18,
            },
            {
                "name": "Kitchen Storage Set",
                "description": "Useful storage containers for organized kitchens.",
                "category": "Home",
                "price": 699,
                "image": "https://images.unsplash.com/photo-1556911220-bff31c812dba",
                "stock": 25,
            },
            {
                "name": "Decorative Plant",
                "description": "Beautiful indoor decorative plant for home.",
                "category": "Home",
                "price": 499,
                "image": "https://images.unsplash.com/photo-1485955900006-10f4d324d411",
                "stock": 20,
            },


            # =========================
            # FOOTWEAR
            # =========================

            {
                "name": "Women's Sandals",
                "description": "Comfortable sandals for women.",
                "category": "Footwear",
                "price": 799,
                "image": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2",
                "stock": 20,
            },
            {
                "name": "Women's Heels",
                "description": "Stylish heels for parties and special occasions.",
                "category": "Footwear",
                "price": 1299,
                "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff",
                "stock": 15,
            },
            {
                "name": "Men's Running Shoes",
                "description": "Lightweight running shoes for daily workouts.",
                "category": "Footwear",
                "price": 1599,
                "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff",
                "stock": 18,
            },
            {
                "name": "Men's Casual Shoes",
                "description": "Comfortable casual shoes for everyday use.",
                "category": "Footwear",
                "price": 1399,
                "image": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77",
                "stock": 20,
            },
            {
                "name": "Sneakers",
                "description": "Trendy sneakers for casual outfits.",
                "category": "Footwear",
                "price": 1799,
                "image": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2",
                "stock": 15,
            },


            # =========================
            # GAMING
            # =========================

            {
                "name": "Gaming Headset",
                "description": "Gaming headset with microphone and surround sound.",
                "category": "Gaming",
                "price": 2999,
                "image": "https://images.unsplash.com/photo-1599669454699-248893623440",
                "stock": 15,
            },
            {
                "name": "Gaming Mouse",
                "description": "High precision mouse designed for gaming.",
                "category": "Gaming",
                "price": 1499,
                "image": "https://images.unsplash.com/photo-1527814050087-3793815479db",
                "stock": 20,
            },
            {
                "name": "Gaming Keyboard",
                "description": "RGB mechanical keyboard for gaming.",
                "category": "Gaming",
                "price": 2499,
                "image": "https://images.unsplash.com/photo-1595225476474-87563907a212",
                "stock": 12,
            },
            {
                "name": "Game Controller",
                "description": "Wireless controller for gaming and entertainment.",
                "category": "Gaming",
                "price": 1999,
                "image": "https://images.unsplash.com/photo-1600080972464-8e5f35f63d08",
                "stock": 15,
            },

        ]

        # Add or update every product
        for item in products:
            Product.objects.update_or_create(
                name=item["name"],
                defaults={
                    "description": item["description"],
                    "category": item["category"],
                    "price": item["price"],
                    "image": item["image"],
                    "stock": item["stock"],
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Product catalogue loaded successfully! {len(products)} products processed."
            )
        )