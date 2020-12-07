'''
-------------------------------------------------------------------------------
Name:	problem2.py

Purpose: To take the amount of chicken and the number of kids as input and gives you the amount of chicken that each student will recieve along with the remainder of the chicken that is given to Mr. Fabroa as output.

Author: Chung.C

Created: 07/12/2020
------------------------------------------------------------------------------
'''

#Input number of chicken and kids
chicken = float(input("Enter number of chicken: "))
students = float(input("Enter number of kids: "))

#Using the number of chickens distribute it among the class
distribution = chicken//students
fabroa_chicken = distribution%students

#Output the number of chicken that each student will get and the amount of chicken Mr.Fabroa will get
print("This is how many pieces each kid will get: " + str(distribution) + " This is how many pieces of chicken Mr. Fabroa will get: " + str(fabroa_chicken))