
# Project 01: Calculator 
# Topic: Calculator Project(Planning and Structure)
# Description: Learning how to build a simple calculator project using Python.
# Author: Nasir Ali 

# What is a Calculator?
# A calculator project is a simple program that performs mathematical operations based on the user choice.

# Menu Function 
#Display all available calculator options.

def menu():
	print("=" * 30)
	print("Simple Calculator")
	print("=" * 30)
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	print("5. Squaring")
	print("6. Cube")
	print("7. Power")
	print("8. Exit")
	print("=" * 30)
	print()


# Addition Function 
#Takes two numbers from user and displays their sum

def addition():
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	result = num1+num2
	print(f"Answer = {result}")
	print("=" * 30)
# Subtraction 
def subtraction():
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	result = num1- num2
	print(f"Answer = {result}")
	print("=" * 30)
# Multiplication 
def multiplication():
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	result = num1 * num2
	print(f"Answer = {result}")
	print("=" * 30)

# Division 
def division():
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	if num2 == 0:
		print("Cannot divide by 0")
		return 
	result = num1 / num2
	print(f"Answer = {result}")
	print("=" * 30)

# Square
def squaring():
	num = float(input("Enter a number: "))
	result = num ** 2
	print(f"Answer = {result}")
	print("=" * 30)	

# Cube
def cube():
	num = float(input("Enter a number: "))
	result = num ** 3
	print(f"Answer = {result}")
	print("=" * 30)

# Power 
def power():
	base = float(input("Enter a base number: "))
	exponent = float(input("Enter a exponent number: "))
	result = base ** exponent
	print(f"Answer = {result}")
	print("=" * 30)

while True:
	menu()
	choice = input("choose an option: ")
	if choice == "1":
		addition()
	elif choice == "2":
		subtraction()
	elif choice == "3":
		multiplication()
	elif choice == "4":
		division()
	elif choice == "5":
		squaring()
	elif choice == "6":
		cube()
	elif choice == "7":
		power()
	elif choice == "8":
		print("Thank you for using the Calculator.")
		
		break 
	
	else:
		print("Invalid choice! Please try again")