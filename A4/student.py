class Student:

    def __init__(self, f_name: str, l_name: str, student_num: str, status: bool):
        if not (f_name.isalpha() and l_name.isalpha()):
            raise ValueError("Please enter a first and last name with alphabetic characters!")
        else:
            self.__first_name = f_name.strip().title()
            self.__last_name = l_name.strip().title()

        if not (student_num[0].upper() == "A" and student_num[1:].isdigit() and len(student_num) == 9):
            raise ValueError("Please enter a student number beginning in 'A' following by 8 digits.")
        else:
            self.__id = student_num.upper()

        self.__status = status
        self.__final_grades = []

    def get_f_name(self):
        return self.__first_name

    def get_l_name(self):
        return self.__last_name

    def get_id(self):
        return self.__id

    def get_standing(self):
        return self.__status

    def get_final_grades(self):
        return self.__final_grades

    def set_f_name(self, new_f_name: str):
        if not new_f_name.isalpha():
            raise ValueError("New first name must be alphabet characters!")
        else:
            self.__first_name = new_f_name.strip().title()

    def set_l_name(self, new_l_name: str):
        if not new_l_name.isalpha():
            raise ValueError("New first name must be alphabet characters!")
        else:
            self.__first_name = new_l_name.strip().title()

    def set_standing(self, new_standing):
        if type(new_standing) != bool:
            raise ValueError("Standing must be True or False!")
        else:
            self.__status = new_standing

    def set_grades(self, grade):
        if type(grade) == str:
            raise TypeError("Grade must be an integer!")
        else:
            self.get_final_grades().append(grade)

    def __str__(self):
        return self.__last_name + " " + self.__first_name + " " + self.__id + " " + str(self.__status) \
               + " " + " ".join(str(grade) for grade in self.__final_grades)
