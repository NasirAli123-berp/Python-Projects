
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
	print("6. Check Duplicate ID ")
	print("7. Search by ID")
	print("8. Total Student Count ")
	print("9. Average Age ")
	print("10. Save to CSV")
	print("11. Load from CSV")
	print("12. Exit ")
	print("=" * 30)


students = []
	
#1. Add Student
def add_student():
	student_id = input("Enter Id: ")
	name = input("Enter Name: ")
	try:
		age = int(input("Enter Age: "))
	except ValueError:
		print("Please enter age in numbers only!")
		return 
	city = input("Enter City: ")
	student = {
		"student_id": student_id,
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
			print("student_id", student["student_id"])
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
			student["student_id"] = input("Enter New Id: ")
			student["name"] = input("Enter New Name: ")
			student["age"] = int(input("Enter New Age: "))
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
	
#6. Check Duplicate ID and Add 
	
def add_student():
    student_id = input("Enter Id: ")

    for student in students:
        if student["student_id"] == student_id:
            print("Duplicate ID! Student already exists.")
            return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    city = input("Enter City: ")

    students.append({
        "student_id": student_id,
        "name": name,
        "age": age,
        "city": city
    })
    print("Student Added Successfully!")
  
#7. Search by Id 
def search_by_id():
   search_id = input("Enter Student ID: ")

   for student in students:
       if student["student_id"] == search_id:
           print(student)
           return

   print("Student Not Found")
   
#8. Total Student Count

def total_students():
    print("Total Students:", len(students))
    
#9. Average Age

def average_age():
    if len(students) == 0:
        print("No Students Found")
        return

    total = 0
    for student in students:
        total += int(student["age"])

    avg = total / len(students)
    print("Average Age:", avg)


#10. Save to CSV   
import csv

def save_csv():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["student_id", "name", "age", "city"])

        for student in students:
            writer.writerow([
                student["student_id"],
                student["name"],
                student["age"],
                student["city"]
            ])

    print("Data Saved Successfully!")

 
#11. Load CSV

import csv

def load_csv():
    students.clear()

    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append({
                    "student_id": row["student_id"],
                    "name": row["name"],
                    "age": row["age"],
                    "city": row["city"]
                })

        print("Data Loaded Successfully!")

    except FileNotFoundError:
        print("CSV File Not Found")  
        
          
# Main Function 
 
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
		add_student()
	elif choice == "7":
		search_by_id()
	elif choice == "8":
		total_students()
	elif choice == "9":
		average_age()
	elif choice == "10":
		save_csv()
	elif choice == "11":
		load_csv()
	elif choice == "12":
		print("Thank you for using ")
		break 
	else:
		print("Invalid Choice ")
		
			
			
			