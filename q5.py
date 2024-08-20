class Student:
    def __init__(self, name, age, roll_num):
        self._name = name
        self._age = age
        self._roll_num = roll_num
    
    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Age : {self._age}")
        print(f"Roll Number: {self._roll_num}")

    # Setter Methods
    def set_name(self,name):
        self._name = name
    def set_age(self,age):
        self._age = age
    def set_roll_num(self, roll_num):
        self.roll_num = roll_num

    # Getter Methods
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_roll_num(self):
        return self._roll_num
    
    # Update the details of students
    def update_details(self, name, age, roll_num):
        self._name = name
        self._age = age
        self._roll_num = roll_num

def Student_data():
    print("Operations: ")
    print("1. Display Student Info.")
    print("2.Update Student info.")
    print("3.Get data of student")
    # print("4.Update Specific data of student")
    print("5. Exit the Program")

    while True:
        if __name__ == '__main__':
            student1 = Student("Chris Evans", 21, 2044)
            student2 = Student("Steve Smith", 25, 3056)

            choice = input("Enter a number between 1 to 5 to perform a specific operation: ")
            if choice in ('1','2','3','4','5'):
                if choice != '5':

                # Display Student records
                    if choice == '1':
                        student1.display_info()
                        print()
                        student2.display_info() 
                        print()
                    
                # Updating Student records
                    elif choice == '2':
                        update_no_ = input("Enter which student's record needs to be updated (1/2): ")
                        if update_no_ == '1':
                            name = input("Enter name")
                            age = input("Enter age")
                            roll_num = input("Enter roll no.")
                            student1.update_details(name, age, roll_num)
                        elif update_no_ == '2':
                            name = input("Enter name")
                            age = input("Enter age")
                            roll_num = input("Enter roll no.")
                            student2.update_details(name, age, roll_num)

                    # elif choice == '3':
                    #     student1.get_name()
                    #     student1.get_age()
                    #     student1.get_roll_num()

                else:
                    print("Program ends")
                    break

            else:
                print("Invalid Opeartion: Enter a no. between 1 to 5")


Student_data()