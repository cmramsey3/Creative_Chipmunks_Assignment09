# File Name : main.py
# Student Name: Colton Ramsey, Alisha Siddiqui, Daquan Daniels
# email: ramseyc6@mail.uc.edu, siddiqas@mail.uc.edu, danieldu@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/03/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: will work in teams to develop a VS project that accesses our SQL Server
# instance, extracts some data from the *Grocery Store Simulator database, and produces some
# interesting results.

# Brief Description of what this module does: Contains the main code that will be run to execute the instructions 
# in the assignment.
# Citations: Google Gemini
# Anything else that's relevant: None

from dataManagementpackage.dataManagement import *
import random

if __name__ == "__main__":

    # Initialize the Class as an object
    db_manager = DatabaseAssignment('Driver={SQL Server};'
                                 'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                                 'Database=GroceryStoreSimulator;'
                                 'uid=IS4010Login;'
                                 'pwd=P@ssword2;'
                                 ) # Given Database Doc String

    #1
    products = db_manager.fetch_products()

    #2
    selected_product = random.choice(products)

    product_id = selected_product[0]
    description = selected_product[2]
    manufacturer_id = selected_product[3]
    brand_id = selected_product[4]

    #3-4
    manufacturer_name = db_manager.get_manufacturer_name(manufacturer_id)

    #5
    brand_name = db_manager.get_brand_name(brand_id)

    #6
    items_sold = db_manager.get_items_sold(product_id) 

    #7
    print(f"{description} from {manufacturer_name} under the {brand_name} brand has sold {items_sold} units.")


