class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def save_to_file(self):
        with open("student.txt","a") as f:
            f.write(f"{self.name},{self.marks}\n")

    @staticmethod
    def result():
        with open("student.txt","r") as f:
            for line in f:
                name, marks = line.strip().split(",")
                print(f"Name: {name}, Marks: {marks}")

# Create objects
s1 = Student("Alice", 85)
s2 = Student("Bob", 90)

# Save to file
s1.save_to_file()
s2.save_to_file()

# Read all data
Student.result()