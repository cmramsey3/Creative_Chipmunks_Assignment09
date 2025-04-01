import pyodbc
import random 

def connect_to_database(self):
        """
        Connect to our SQL Server instance
        @return connection object
        """
        conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=GroceryStoreSimulator;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;'
        )
        return conn

class ProductRepository:#Daquan
    """Handles retrieving product data from the database."""
    
    def __init__(self, db_connector):
        self.db = db_connector

class ProductService: #Daquan
    """Handles business logic related to product selection."""
    
    def __init__(self, product_repo):
        self.product_repo = product_repo

class ManufacturerRepository: #Daquan
    """Handles retrieving manufacturer information."""
    
    def __init__(self, db_connector):
        self.db = db_connector

class ManufacturerService: #Questiom 4
    """Handles business logic related to manufacturer retrieval."""


class BrandRepository: #Question 5
    """Handles retrieving brand information."""


class SalesRepository: #Question 6
    """Handles retrieving sales data."""

class SentenceService: #Question 7 
    """Handles constructing the final output sentence.""" 