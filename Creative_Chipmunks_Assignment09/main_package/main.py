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

if __name__ == "__main__":
    pass


import pyodbc
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
