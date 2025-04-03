# File Name : dataManagement.py
# Student Name: Colton Ramsey, Alisha Siddiqui, Daquan Daniels
# email: ramseyc6@mail.uc.edu, siddiqas@mail.uc.edu, danieldu@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/03/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Working in teams to develop a VS project that accesses our SQL Server
# instance, extracts some data from the *Grocery Store Simulator database, and produces some interesting results.

# Brief Description of what this module does: Holds the class we created that works with the data
# inside of the given database
# Citations: Google Gemini
# Anything else that's relevant: None

import pyodbc
import random

class DatabaseAssignment:
    """
    Contains the functions created to work with data from a given database
    """
    def __init__(self, connection_string):
        """
        Constructor that stores the connection string give from the instantiation in self.
        @return None
        """
        self.connection_string = connection_string
        

    def get_connection(self):
        """
        Establishes and returns a database connection.
        @return database connection
        """
        return pyodbc.connect(self.connection_string)

    def fetch_products(self):
        """
        Retrieve product data from tProduct. Uses the given SQL query in the assignment
        @return list
        """
        query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data

    def get_manufacturer_name(self, manufacturer_id):
        """
        Retrieves the manufacturer name based on ManufacturerID.
        @param manufacturer_id: wanted manufacturer_id to lookup the correct manufacturer_name
        @return string
        """
        query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}"
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        manufacturer_name = cursor.fetchone()
        conn.close()
        return manufacturer_name[0]

    def get_brand_name(self, brand_id):
        """
        Retrieves the brand name based on BrandID.
        @param brand_id: wanted brand_id to lookup the correct brand_name
        @return string
        """
        query = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}"
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        brand_name = cursor.fetchone()
        conn.close()
        return brand_name[0]

    def get_items_sold(self, product_id):
        """
        Retrieves the total number of items sold for a given ProductID using the given SQL query.
        @param product_id: wanted product id to sum
        @return int
        """
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
        return items_sold[0]
