
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
	print("8. Average")
	print("9. Percentage")
	print("10. Modulus")
	print("11. Floor Division")
	print("12. Square Root")
	print("13. Maximum")
	print("14. Minimum")
	print("15. Absolute")
	print("16. Check Even & Odd Numbers")
	print("17. Exit")
	print("=" * 30)
	print()

#Helper Show Result 
def show_result(result):
	print("=" * 30)
	print(f"Answer = {result}")
	print("=" * 30)
# Helper Show Input Numbers 
def get_numbers():
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	return num1, num2

#1. Addition Function 
#Takes two numbers from user and displays their sum

def addition():
	num1,num2 = get_numbers()
	result = num1+num2
	show_result(result)
	
#2. Subtraction 
def subtraction():
	num1,num2 = get_numbers()
	result = num1- num2
	show_result(result)
	
#3. Multiplication 
def multiplication():
	num1,num2 = get_numbers()
	result = num1 * num2
	show_result(result)

#4. Division 
def division():
	num1,num2 = get_numbers()
	if num2 == 0:
		print("Cannot divide by 0")
		return 
	result = num1 / num2
	show_result(result)

#5. Square
def square():
	num = float(input("Enter a number: "))
	result = num ** 2
	show_result(result)	

#6. Cube
def cube():
	num = float(input("Enter a number: "))
	result = num ** 3
	show_result(result)

#7. Power 
def power():
	base = float(input("Enter a base number: "))
	exponent = float(input("Enter a exponent number: "))
	result = base ** exponent
	show_result(result)

#8. Average
def average():
	num1,num2 = get_numbers()
	result = (num1+num2)/2
	show_result(result)
	
#9. Percentage (%)
def percentage():
	total_marks = float(input("Enter total marks: "))
	obtain_marks = float(input("Enter obtained marks: "))
	if total_marks == 0:
		print("total_marks cannot be zero")
		return 
	result = (obtain_marks / total_marks)*100
	show_result(result)
	
#10. Modulus
def modulus():
	num1,num2 = get_numbers()
	result = num1 % num2
	show_result(result)
	
#11. Floor Division 
def floor_division():
	num1,num2 = get_numbers()
	if num2 == 0:
		print("cannot floor division by zero")
		return 
	result = num1 // num2
	show_result(result)
	
#12. Square Root
import math 
def square_root():
	num = float(input("Enter a number: "))
	if num < 0:
		print("Square root of a nagetive number is not possible")
		return 
	result = math.sqrt(num)
	show_result(result)
	
#13. Maximum 
def maximum():
	num1,num2 = get_numbers()
	result = max(num1,num2)
	show_result(result)
	
#14. Minimum 
def minimum():
	num1,num2 = get_numbers()
	result = min(num1,num2)
	show_result(result)
#15. Absolute 
def absolute():
	num = float(input("Enter a number: "))
	result = abs(num)
	show_result(result)
	
#16. Check Even & Odd Numbers 
def check_even_odd():
	num = int(input("Enter a number: "))
	if num %2 == 0:
		print("Even")
	else:
		print("Odd")
	
		
				
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
		square()
	elif choice == "6":
		cube()
	elif choice == "7":
		power()
	elif choice == "8":
		average()
	elif choice == "9":
		percentage()
	elif choice == "10":
		modulus()
	elif choice == "11":
		floor_division()
	elif choice == "12":
		square_root()
	elif choice == "13":
		maximum()
	elif choice == "14":
		minimum()
	elif choice == "15":
		absolute()
	elif choice == "16":
		check_even_odd()
	elif choice == "17":
		print("Thank you for using Calculator ")
		break 
	
	else:
		print("Invalid choice! Please try again")
	
	