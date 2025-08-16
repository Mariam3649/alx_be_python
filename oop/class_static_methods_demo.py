class Student:
    school_name = "ALX School"   # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def display_info(self):
        return f"Student: {self.name}, Age: {self.age}, School: {Student.school_name}"

    # class method
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # static method
    @staticmethod
    def is_adult(age):
        return age >= 18
def main():
    s1 = Student("Mariam", 20)
    s2 = Student("Ali", 16)

    print(s1.display_info())
    print(s2.display_info())

    Student.change_school("New ALX")
    print(s1.display_info())

    print("Is 20 adult?", Student.is_adult(20))
    print("Is 16 adult?", Student.is_adult(16))


if __name__ == "__main__":
    main()
