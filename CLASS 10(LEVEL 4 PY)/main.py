class BillingSystem:

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.__total_bill = 0
        self.products = []

    def add_to_cart(self, product_name, price):
        self.products.append((product_name, price))
        self.__total_bill += price
        print(f"Product (product_name) added to cart for TK - (price)")

    def show_cart(self):
        print(f"Customer - {self.customer_name} has added following items to cart \n")
        for i, (product, price) in enumerate(self.products, start=1):
            print(f"{i}. {product} for {price} TK")

    def show_total_bill(self):
        print(f"Total Bill for customer - {self.customer_name} is - {self.__total_bil} TK")

    def apply_discount(self):
        self.__discount_applied = False
        if self.__discount_applied:
            print("Discount already applied")
            return

        if self.__total_bill = 10000:
            discount = self.__total_bill * 0.05
            self.__total_bill -= discount
            print(f"Customer - {self.customer_name} got 5% discount")
            print(f"Discount Amount: {discount:.2f} TK")
            print(f"Total Bill After Discount: {self.__total_bill:.2f} TK")
        else:
            print(f"Customer - {self.customer_name} does not qualify for discount")

    def finalize_bill(self):
        print("\n---------Final Bill--------")
        print(f"Customer - {self.customer_name}")
        self.apply_discount()
        self.show_cart()
        self.show_total_bill()
        print("-------THANK YOU-------")
        
customer = BillingSystem(input("Enter customer name - "))

while true:
    print("\n----------Menu-----------")
    print("1. Add to cart")
    print("2. Show cart")
    print("3. Show total bill)
    print("4. Apply discount")
    print("5. Finalize bill")
    print("6. Exit")

    choice = int(input("Enter choice - "))

    if choice == 1:
        product_name = input("Enter product name - ")
        price = float(input("Enter price - "))
        customer.add_(product_name, price)
    elif choice == 2:
        customer.show_cart()
    elif choice == 3:
        customer.show_total_bill()
    elif choice == 4:
        customer.apply_discount()
    elif choice== 5:
        customer.finalize_bill()
    elif choice == 6:
        break

else:
print("Invalid choice")


    

