
#Topic : Student Management System
#Description : A simple system to store, search, update and delete student records using Python.
#Author: Nasir Ali

# Menu Function
def menu():
	print("=" * 30)
	print("Student Management system")
	print("=" * 30)
	print("1. Add Student")
	print("2. Show Student")
	print("3. Search Student")
	print("4. Update Student")
	print("5. Delete Student")
	print("6. Exit ")
	print("=" * 30)


students = []
	
#1. Add Student
def add_student():
	id = input("Enter Id: ")
	name = input("Enter Name: ")
	age = input("Enter Age: ")
	city = input("Enter City: ")
	student = {
		"id":id,
		"name":name,
		"age":age,
		"city":city
	}
	students.append(student)
	print("Student added successfully ")
	
#2. Show Student

def show_students():
	if len(students) == 0:
		print("No Student Found!\n")
	else:
		for student in students:
			print("=" * 30)
			print("id", student["id"])
			print("name", student["name"])
			print("age", student["age"])
			print("city", student["city"])
			
#3. Search Student
 
def search_student():
	search = input("Enter student name: ")
	found = False
	for student in students:
			if student["name"] == search:
				print(student)
				found = True 
	if found == False:
			print("Student Not Found!\n")

#4. Update Student

def update_student():
	search = input("Enter Student Name: ")
	for student in students:
		if student["name"] == search:
			print("Student Found! ")
			student["id"] = input("Enter New Id: ")
			student["name"] = input("Enter New Name: ")
			student["age"] = input("Enter New Age: ")
			student["city"] = input("Enter New City: ")
			print("Student Update Successfully!\n")
			return 
	print("Student Not Found!\n")
			
			
#5. Delete Student 

def delete_student():
	search = input("Enter Student Name: ")
	for student in students:
		if student["name"] == search:
			students.remove(student)
			print("Student Deleted")
			return 
	print("Student Not Found")
	
while True:
	menu()
	choice = input("Choice Option: ")
	if choice == "1":
		add_student()
	elif choice == "2":
		show_students()
	elif choice =="3":
		search_student()
	elif choice == "4":
		update_student()
	elif choice == "5":
		delete_student()
	elif choice == "6":
		print("Thank you for using ")
		break 
	else:
		print("Invalid Choice ")
		
			
			
			