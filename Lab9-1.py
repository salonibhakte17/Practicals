class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    def get_data(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display(self):
        print("\nName:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    pass

managers = []
for i in range(10):
    print(f"\nEnter details of Manager {i+1}")
    m = Manager("", 0, 0, "")
    m.get_data()
    managers.append(m)

print("\n--- Manager Details ---")
for m in managers:
    m.display()