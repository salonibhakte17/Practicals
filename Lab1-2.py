vendor_name = input("Enter vendor name: ")
year = int(input("Enter year of association: "))
contact = input("Enter contact number: ")
email = input("Enter email ID: ")

total_purchase = 0
for month in range(1, 13):
    amount = float(input(f"Enter purchase amount for month {month}: "))
    total_purchase += amount

print("\n--- Vendor Details ---")
print("Vendor Name:", vendor_name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)

print("\nAnnual Purchase/Billing Report")
print("Total Annual Purchase: Rs.", total_purchase)