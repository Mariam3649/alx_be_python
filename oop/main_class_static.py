from class_static_methods_demo import Student

def main():
    s1 = Student("Mariam", 20)
    s2 = Student("Omar", 16)

    # قبل تغيير اسم المدرسة
    print(s1.display_info())
    print(s2.display_info())

    # استخدام class method
    Student.change_school("Holberton School")
    print(s1.display_info())
    print(s2.display_info())

    # استخدام static method
    print(f"Is {s1.name} an adult? {Student.is_adult(s1.age)}")
    print(f"Is {s2.name} an adult? {Student.is_adult(s2.age)}")

if __name__ == "__main__":
    main()

