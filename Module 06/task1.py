students_marks={
    "Alice":90,
    "Chidatma":95,
    "Rahul":80,
}

name = input("Enter a name: ").title()

if name in students_marks:
    print(f"{name}'s marks: {students_marks[name]}")
else:
    print("Student not found.")