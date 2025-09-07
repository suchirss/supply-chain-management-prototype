from CRUD_functions import *

ORDERS_TABLE = "orders"

class OrderPlacementProgram:

    def __init__(self):
        print("Welcome to the order placement program!")
        self.__get_initial_input()

    def __get_initial_input(self):
        print("Which of the following would you like to do?: \n" \
        "1) place an order \n" \
        "2) check order status \n" \
        "3) cancel an order \n" )

        # good test: enter a number with spaces
        initialChoice = str(input("Enter a number: "))
        print(initialChoice)
        if initialChoice != "1" and initialChoice != "2" and initialChoice != "3":
            input("Please enter a number only. Press enter to continue \n") 
            self.__get_initial_input()
        elif initialChoice == "1":
            self.__get_order_input()
        else:
            print("This part of the page is still in construction 😬")

    def __get_order_input(self):
        self.order_name = input("Enter the name of the product you would like to order: \n")
        # TODO: checking if product actually exists in warehouse

        self.quantity = int(input("Enter the quantity you would like to order: \n"))
        self.client_name = input("Enter the name of the organization ordering this product: \n")

        self.__add_order_to_db(self.client_name, self.order_name, self.quantity)

    def __add_order_to_db(self, client_name, order_name, quantity):
        create_order(client_name=client_name, product_name=order_name, SKU=0000, quantity=quantity,status="Processing")
        # TODO: check SKU with warehouse
        print("Added order to supply_chain database")

        # print(retrieve_order(ORDERS_TABLE, "order_id", client_name, order_name))
        # print("Please retain this reference number for your records: ", )

    # def __get_and_print_order_id(self):
        

        
    # create setters that the user cannot run directly (private - name mangled)
    # create internal private functions for order verification
    # create getters that allow the user to see their order history (based on the client name)

OrderPlacementProgram()