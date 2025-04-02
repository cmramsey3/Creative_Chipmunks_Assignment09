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
# Citations:
# Anything else that's relevant:

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

    # Step 1: Fetch product data
    products = db_manager.fetch_products()

    # Step 2: Randomly select one product
    selected_product = random.choice(products)

    # Store variables
    product_id = selected_product[0]
    description = selected_product[2]
    manufacturer_id = selected_product[3]
    brand_id = selected_product[4]

    # Step 3-4: Get manufacturer name
    manufacturer_name = db_manager.get_manufacturer_name(manufacturer_id)

    # Step 5: Get brand name
    brand_name = db_manager.get_brand_name(brand_id)

    # Step 6: Get number of items sold
    items_sold = db_manager.get_items_sold(product_id)

    # Step 7: Construct and print the output sentence
    output_sentence = f"The product '{description}' from {manufacturer_name} under the {brand_name} brand has sold {items_sold} units."
    print(output_sentence)


