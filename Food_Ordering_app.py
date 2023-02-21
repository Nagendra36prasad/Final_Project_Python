# Food Ordering app for a restaurant
# The application will have a log-in for admin and users to log-in
# Admin ---> 1.Add new food items. Food Items:name, quantity, price, discount, stock
#            2. Edit food items using FoodID.
#            3.View the list of all food items.
#            4. Remove a food item from the menu using FoodID.

# User ---> 1. Register on the application. Following to be entered for registration:full name, phone number, email, address, password
#           2. Log in to the application
#           3. The user will see 3 options:Place New Order,Order History,Update Profile    
#           4. Place New Order: The user can place a new order at the restaurant.
            # Show list of food. The list item should as follows:
            # Tandoori Chicken (4 pieces) [INR 240]
            #  Vegan Burger (1 Piece) [INR 320]
            # Truffle Cake (500gm) [INR 900]
#           5. Users should be able to select food by entering an array of numbers. For example, if the user wants to order Vegan Burger and Truffle Cake they should enter [2, 3]
#           6. Once the items are selected user should see the list of all the items selected. The user will also get an option to place an order.
#           7. Order History should show a list of all the previous orders
#           8. Update Profile: the user should be able to update their profile            

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
        self.food_ID = 0 # function to generate unique ID


class Admin:
    def __init__(self):
        self.food_items = []
    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name =name, quantity = quantity, price = price , discount = discount, stock =stock)
        food_item.food_ID = len(self.food_items) + 1
        self.food_items.append(food_item)

    def edit_food_item(self, food_ID, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_ID == food_ID:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                

    def view_food_items(self):
        for food_item in self.food_items:
            print(f"ID: {food_item.food_ID}, Name: {food_item.name}, Quantity: {food_item.quantity}, Price: {food_item.price}, Discount: {food_item.discount}, Stock: {food_item.stock}")
            
    
    def remove_food_item(self, food_ID):
        for food_item in self.food_items:
            if food_item.food_ID == food_ID:
                self.food_items.remove(food_item)


class User(Admin):
    def init(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    def login(self):
        input_username = input("Enter your username: ")
        input_password = input("Enter your password: ")
        if input_username == self.full_name and input_password == self.password:
            print("Login Successful!")
            return True
        else:
            print("Incorrect Password.")
            while True:
                option = input("Do you want to try again? (Y/N)").upper()
                if option == "Y":
                    input_username = input("Enter your username: ")
                    input_password = input("Enter your password: ")
                    if input_username == self.full_name and input_password == self.password:
                        print("Login Successful!")
                        return True
                    else:
                        print("Incorrect Password.")
                elif option == "N":
                    print("Exiting...")
                    return False
                else:
                    print("Invalid option. Please try again.")

    def place_new_order(self, food_ids):
        total_cost = 0
        selected_items = []
        for food_item in admin.food_items:
            if food_item.food_ID in food_ids:
                total_cost += food_item.price
                selected_items.append(food_item)
        print("Selected Items:")
        for item in selected_items:
            print(f"{item.name} ({item.quantity}) [INR {item.price}]")
        print(f"Total Cost: INR {total_cost}")
        confirm = input("Do you want to place the order? (Y/N): ")
        if confirm == "Y":
            self.orders.append(selected_items)
            for item in selected_items:
                item.stock -= 1
            print("Order Placed Successfully!")
        else:
            print("Order Cancelled.")

    def order_history(self):
        for i, order in enumerate(self.orders):
            print(f"Order {i+1}:")
            for item in order:
                print(f"{item.name} ({item.quantity}) [INR {item.price}]")
            print()


    def update_profile(self, full_name=None, phone_number=None, email=None, address=None, password=None):
        if full_name:
            self.full_name = full_name
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        if address:
            self.address = address
        if password:    
            self.password = password


# Add food items
food_item1 = FoodItem("Tandoori Chicken", "4 pieces", 240, 0, 10)
food_item2 = FoodItem("Vegan Burger", "1 Piece", 320, 5, 5)
food_item3 = FoodItem("Truffle Cake", "500gm", 900, 10, 2)

admin = Admin()
admin.add_food_item(food_item1.name, food_item1.quantity, food_item1.price, food_item1.discount, food_item1.stock)
admin.add_food_item(food_item2.name, food_item2.quantity, food_item2.price, food_item2.discount, food_item2.stock)
admin.add_food_item(food_item3.name, food_item3.quantity, food_item3.price, food_item3.discount, food_item3.stock)

# Editing a food item
admin.edit_food_item(2, "Vegan Cheeseburger", "1 piece", 350, 20, 30)

# view food items
admin.view_food_items()

# Removing a food item
admin.remove_food_item(1)


user1 = User()   # create a user object
user1.init("Nagendra", "9740450171", "prasadrnag@gmail.com", "123, kolar ", "1234")

# user login with username and Possword
if user1.login():
    print("Welcome, " + user1.full_name)
else:
    print("Please enter the correct username and password.")

#  Place New Order,order history and detials of user
user1.place_new_order([2, 3])                 # select food by entering an array of numbers
user1.order_history() 
print(f"Name: {user1.full_name}, Phone Number: {user1.phone_number}, Email: {user1.email}, Address: {user1.address}, Password: {user1.password}")

# user profile update
user1.update_profile(full_name="prasad", email="prasad.nag@example.com")

