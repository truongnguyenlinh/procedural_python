from student import Student


def obtain_standing() -> bool:
    """Confirm student's current standing.

    RETURN True if user input is Y, False if N"""
    input_standing = input("Is the student in good standing (Y/N)?")
    if input_standing.strip().upper() == "Y":
        return True
    elif input_standing.strip().upper() == "N":
        return False
    else:
        print("Please enter one of the listed options by number!")
        return obtain_standing()


def obtain_grades(student: Student):
    """Confirm if user would like to input final grades. Add to final grades list if so.

    PRECONDITION student must be valid class from Student"""
    grades_input = ""
    while grades_input.strip().title() != "None":
        grades_input = input("Enter the student's final grade for a single course. Otherwise, type 'None'.\n")
        try:
            if grades_input.strip().isdigit():
                student.update_grades(int(grades_input))
        except ValueError as e:
            print(e)


def confirm_unique(id_num: str) -> str:
    """Confirm if student number entered is unique.

    PRECONDITION id_num must be same format seen in Student class"""
    try:
        if id_num.strip().upper() in open("students.txt").read():
            print("Please enter a unique student number!")
            id_num = input("Enter the student's id number in the following format, where 'X' is a number: AXXXXXXXX.")
            return confirm_unique(id_num)
        else:
            return id_num
    except FileNotFoundError:
        return id_num


def add_student():
    """Obtain user input to generate a Student instance."""
    first_name = input("Enter the student's first name (must only be alphabetical characters).")
    last_name = input("Enter the student's last name (must only be alphabetical characters).")
    student_num = input("Enter the student's id number in the following format, where 'X' is a number: AXXXXXXXX.")
    try:
        student_instance = Student(first_name, last_name, confirm_unique(student_num), obtain_standing())
        obtain_grades(student_instance)
        file_write(student_instance)
        print("\nStudent was added successfully!\n")
        return True
    except ValueError as e:
        print(e)


def file_read() -> list:
    """Read students.txt and convert every student back to Student class.

    RETURN a list of Student objects"""
    list_of_students = []
    with open("students.txt", "r") as file_object:
        file = file_object.readlines()
    for line in file:
        student_text = line.split()
        student_instance = Student(student_text[0], student_text[1], student_text[2], eval(student_text[3]))
        for grade in student_text[4:]:
            student_instance.update_grades(int(grade))
        list_of_students.append(student_instance)
    return list_of_students


def file_write(student_object: Student) -> bool:
    """Append student_object to the end of students.txt file.

    PARAM student_object must be an instance of class Student
    RETURN True if student_object was successfully appended to file"""
    filename = "students.txt"
    # FileNotFoundError will never occur, as 'a' mode will always create a new file if not existing
    with open(filename, "a") as file_object:
        file_object.write(student_object.__str__() + "\n")
    return True


def file_delete_student(student_num: str) -> bool:
    """Determine if student was removed from text-file.

    PRECONDITION student_num must be formatted as seen in Student ID attribute
    RETURN True if student_num is not found on file, False otherwise"""
    file_object = open("students.txt", "r")
    file = file_object.read()
    file_object.close()
    if student_num not in file:
        return True
    else:
        return False


def exclude_student(stud_list: list):
    """Create new file excluding line with student_num.

    PRECONDITION student_list must be list of Student objects"""
    with open("students.txt", "r+") as file_object:
        for student in stud_list:
            file_object.write(student.__str__() + "\n")
        file_object.truncate()


def del_student():
    """Delete a Student from students.txt given their student number."""
    student_num = input("Enter the student number you would like to remove.")
    student_num = student_num.strip().title()

    if not (len(student_num.upper()) == 9 and student_num[1:].isdigit() and student_num.upper()[0] == "A"):
        print("Please enter a student number beginning with 'A', followed by 8 digits.")
    elif file_delete_student(student_num):
        print("This student is no longer on file.")
    else:
        student_list = file_read()
        for student in student_list:
            if student.get_id() == student_num:
                student_list.remove(student)
        print("Deleted!")
        exclude_student(student_list)


def calc_average():
    """Calculate the average of all students in students.txt, excluding students with no grades."""
    students_list = file_read()
    count = 0
    class_avg = []
    try:
        for student in students_list:
            if len(student.get_final_grades()) != 0:
                count += 1
                class_avg.append(student.get_gpa())
        print("The class average is " + str(round((sum(class_avg) / count), 2)) + "%.\n")
    except ZeroDivisionError:
        print("The class currently has no grades!")


def print_class_list():
    """Print all students in students.txt file."""
    students_list = file_read()
    sorted_students = sorted(students_list, key=lambda student: student.get_f_name())
    for students in sorted_students:
        print(students)


def user_selection(user_input: str):
    """Determine user input to perform action.

    PRECONDITION user_input must be a string within range 1 to 5"""
    if user_input == "1":
        add_student()
    elif user_input == "2":
        del_student()
    elif user_input == "3":
        calc_average()
    elif user_input == "4":
        print_class_list()
    elif user_input == "5":
        quit()
    else:
        print("Please enter a valid action!\n")


def main():
    while True:
        try:
            print("1. Add student\n2. Delete student\n3. Calculate class average\n4. Print class list\n5. Quit\n")
            action_input = input("Enter a menu number that represents your desired action:\n")
            action_input.strip()
            user_selection(action_input)
        except FileNotFoundError:
            print("There are currently no students on file!")


if __name__ == '__main__':
    main()
