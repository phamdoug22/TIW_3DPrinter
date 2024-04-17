"""
    File: in_class_activity_1_oop.py
    Description: This program creates a controller software of for a 
    “Fully Automatic Beverage Vending Machine”. Through it, users can
    selec their preferred coffee (Regular Coffee, Espresso, and Cappuccino)
    and add up to three total condiments (of sugar and milk). After that,
    the program prints what the user ordered and calculates the price for them.
    It also asks the user if they would like to order another drink.

    Student Name: Douglas Pham
    Student UT EID: ddp2328

    Partner Name: Zachary Sepulveda
    Partner UT EID: zrs386

    Course Name: CS 313E
    Unique Number: 50775
    Date Created: 2/05/24
    Date Last Modified: 2/05/24

    Input: Type of coffee and condiments 
    Output: What the user ordered and the price

    python in_class_activity_1_oop.py
"""


class Tool:
    def __init__(self, name, quantity, cost, supplier):
        self.name = name
        self.quantity = quantity
        self.cost = cost
        self.supplier = supplier

    def __str__(self):
        return f"{self.name} - Quantity: {self.quantity}, Cost: ${self.cost:.2f}, Supplier: {self.supplier}"

class Inventory:
    def __init__(self):
        self.tools = {}

    def add_tool(self, tool):
        if tool.name in self.tools:
            print(f"Error: Tool {tool.name} already exists in inventory.")
        else:
            self.tools[tool.name] = tool
            print(f"Tool {tool.name} added successfully.")

    def update_tool(self, name, quantity, cost, supplier):
        if name in self.tools:
            updated_tool = Tool(name, quantity, cost, supplier)
            self.tools[name] = updated_tool
            print(f"Tool {name} updated successfully.")
        else:
            print(f"Error: Tool {name} not found in inventory.")

    def delete_tool(self, name):
        if name in self.tools:
            del self.tools[name]
            print(f"Tool {name} deleted successfully.")
        else:
            print(f"Error: Tool {name} not found in inventory.")

    def search_tool(self, name):
        if name in self.tools:
            print(f"Found: {self.tools[name]}")
        else:
            print(f"Tool {name} not found in inventory.")

    def list_inventory(self):
        print("Current Inventory:")
        for tool in self.tools.values():
            print(tool)

class InventoryController:
    def __init__(self):
        self.inventory = Inventory()

    def get_user_input(self):
        print("\n--- Inventory Management Menu ---")
        print("1. Add Tool")
        print("2. Update Tool")
        print("3. Delete Tool")
        print("4. Search for Tool")
        print("5. List Inventory")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        return choice

    def add_tool(self):
        name = input("Enter tool name: ")
        quantity = int(input("Enter quantity: "))
        cost = float(input("Enter cost per item: "))
        supplier = input("Enter supplier name: ")
        new_tool = Tool(name, quantity, cost, supplier)
        self.inventory.add_tool(new_tool)

    def update_tool(self):
        name = input("Enter tool name to update: ")
        quantity = int(input("Enter new quantity: "))
        cost = float(input("Enter new cost per item: "))
        supplier = input("Enter new supplier name: ")
        self.inventory.update_tool(name, quantity, cost, supplier)

    def delete_tool(self):
        name = input("Enter tool name to delete: ")
        self.inventory.delete_tool(name)

    def search_tool(self):
        name = input("Enter tool name to search for: ")
        self.inventory.search_tool(name)

    def run(self):
        while True:
            user_choice = self.get_user_input()
            if user_choice == '1':
                self.add_tool()
            elif user_choice == '2':
                self.update_tool()
            elif user_choice == '3':
                self.delete_tool()
            elif user_choice == '4':
                self.search_tool()
            elif user_choice == '5':
                self.inventory.list_inventory()
            elif user_choice == '6':
                print("Exiting Inventory Management System.")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 6.")

def main():
    controller = InventoryController()
    controller.run()