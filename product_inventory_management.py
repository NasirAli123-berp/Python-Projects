
#Topic : Inventory Management System
# Description : A simple program 
# Author: Nasir Ali 
import csv

products = []

def menu():
    print("=" * 35)
    print("Inventory Management System")
    print("=" * 35)
    print("1. Add Product")
    print("2. Show Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Total Products")
    print("7. Total Inventory Value")
    print("8. Low Stock Alert")
    print("9. Save to CSV")
    print("10. Load from CSV")
    print("11. Exit")
    print("=" * 35)
    
#1. Add Product 
def add_product():
	pid = input("Enter Product ID: ")
	for product in products:
		if product["id"] == pid:
			print("Product ID Already Exists!")
			return 
	name = input("Enter Product Name: ")
	quantity = int(input("Enter Quantity: "))
	price = float(input("Enter Price: "))
	
	products.append({
	    "id":pid,
	    "name":name,
	    "quantity": quantity,
	    "price": price 
	})
	print("Product Added successfully!")


#2. Show Products

def show_products():
	if len(products) == 0:
		print("No Products Found!")
		return 
	for product in products:
		print(product)
		
#3. Update Product 

def update_product():
	pid = input("Enter product ID: ")
	for product in products:
		if product["id"] == pid:
			product["name"] = input("Enter New Name: ")
			product["quantity"] = int(input("Enter New Quantity: "))
			product["price"] = float(input("Enter New Price: "))
			print("Product Update Successfully!")
			return 
	print("Product Not Found!")

	
#4. Delete Product

def delete_product():
	pid = input("Enter Product ID: ")
	for product in products:
		if product["id"] == pid:
			products.remove(product)
			print("Product Deleted successfully!")
			return 
	print("Product Not Found!")
	

#5. Search Product 

def search_product():
	name = input("Enter Product Name: ")
	for product in products:
		if product["name"].lower()== name.lower():
			print(product)
			return 
	print("Product Not Found!")

#6. Total Product 

def total_products():
	print("Total Product",len(products))

#7. Total  Inventory Value 

def inventory_value():
	total = 0
	for product in products:
		total += product["quantity"] * product["price"]
	print("Total Inventory Value", total)

#8. Low Stock Alert

def low_stock():
	found = False
	for product in products:
		if product["quantity"] < 5:
			print(product)
			found = True 
	if not found:
		print("No Low Stock Products!")

#9. Save to CSV 

def save_csv():
	with open("products.csv","w", newline="") as file:
		writer = csv.writer(file)
		writer.writerow(["ID","Name","Quantity","Price"])
		for product in products:
			writer.writerow([
			    product["id"],
			    product["name"],
			    product["quantity"],
			    product["price"]
			    ])
		print("Data Saved Successfully!")


#10. Load from CSV 
def load_csv():
    products.clear()

    try:
        with open("products.csv", "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:
                products.append({
                    "id": row[0],
                    "name": row[1],
                    "quantity": int(row[2]),
                    "price": float(row[3])
                })

        print("Data Loaded Successfully.")

    except FileNotFoundError:
        print("CSV File Not Found.")
        
# Main Program

while True:

    menu()

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        show_products()

    elif choice == "3":
        update_product()

    elif choice == "4":
        delete_product()

    elif choice == "5":
        search_product()

    elif choice == "6":
        total_products()

    elif choice == "7":
        inventory_value()

    elif choice == "8":
        low_stock()

    elif choice == "9":
        save_csv()

    elif choice == "10":
        load_csv()

    elif choice == "11":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")		