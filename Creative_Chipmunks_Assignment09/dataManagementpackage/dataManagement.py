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

import pyodbc
import random

class DatabaseAssignment:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        

    def get_connection(self):
        """Establish and return a database connection."""
        return pyodbc.connect(self.connection_string)

    def fetch_products(self):
        """Retrieve product data from tProduct."""
        query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data

    def get_manufacturer_name(self, manufacturer_id):
        """Retrieve the manufacturer name based on ManufacturerID."""
        query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}"
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        manufacturer_name = cursor.fetchone()
        conn.close()
        return manufacturer_name[0] if manufacturer_name else "Unknown Manufacturer"

    def get_brand_name(self, brand_id):
        """Retrieve the brand name based on BrandID."""
        query = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}"
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        brand_name = cursor.fetchone()
        conn.close()
        return brand_name[0] if brand_name else "Unknown Brand"

    def get_items_sold(self, product_id):
        """Retrieve the total number of items sold for a given ProductID."""
        query = f"""
        SELECT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
        FROM dbo.tTransactionDetail 
        INNER JOIN dbo.tTransaction 
        ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID 
        WHERE (dbo.tTransaction.TransactionTypeID = 1) 
        AND (dbo.tTransactionDetail.ProductID = {product_id})
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        items_sold = cursor.fetchone()
        conn.close()
        return items_sold[0] if items_sold else 0
