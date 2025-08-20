
students = {}
    
while True:
    print("\n Select Your Option")
    print("\n1. Add Student")
    print("\n2. Update student")
    print("\n3.Remove Student")
    print("\n4. View all Students")
    print("\n5. search a student")
    print("\n6. Show all")
    print("\n7. Exit")

    print("Enter your choice: ")
    n=int(input())
    if n == 1:
        name = input("Enter Name of Student:: ")
        roll = input("Enter Your Number:: ")
        students[roll]=name
        print(f"Student added : {name} : {roll}")

    elif n == '2':
        roll = input("enter roll no to update :: ")
        if roll in students:
            name = input("Enter Updated Name:: ")
            students[roll] = name
            print(f"Student added : {name} : {roll}")
        else:
            print("You entered a wrong roll no")

    elif n == 3:
        roll = input("Enter the roll no of removing student:: ")
        if roll in students:
            removed = students.pop(roll)
            print(f"Removed Student :: {name} : {roll}")

        else:
            print("Roll no not found")
    
    elif n == 4:
        if students:
            print("All Student: ")
            for roll,name in students.items():
                print(f"Roll :: {roll} , Name:: {name}")
            else:
                print("No data in database")
    
    elif n == 5:
        roll = int(input("Enter a roll no :: "))
        if roll in students:
            print(f"Found :: {roll} : {name} ")
        else:
            print("Data not found")

    elif n == 6:
        print(f"Total students:: {len(students)}")
        break
    else:
        print("Invalid choice, recheck the value")





