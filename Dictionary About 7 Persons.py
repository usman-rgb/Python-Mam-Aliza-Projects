def main():
    people_info = {
        "Usman": {"Age": 20, "City": "Dera Ghazi Khan", "Profession": "Student"},
        "Bilal": {"Age": 19, "City": "Muzafargarh", "Profession": "Video Editor"},
        "Lateef": {"Age": 23, "City": "Taunsa", "Profession": "Job"},
        "Subhan": {"Age": 18, "City": "DGK", "Profession": "Middle Class School Student"},
        "Sulman": {"Age": 16, "City": "DGK", "Profession": "Tyre Worker"},
        "Talha": {"Age": 20, "City": "Sindh", "Profession": "Student"},
        "Nohan": {"Age": 28, "City": "Quetta", "Profession": "Python Developer"},
    }

    print("Welcome To The Dictionary:")
    print("Enter The Information about The 7 Persons:")

    while True:
        name = input("Enter The Name of The Person (or 'exit' to Exit): ").capitalize()
        if name == "Exit":
            print("Thank You For Using The Dictionary: Goodbye!")
            break
        elif name in people_info:
            print(f"Information for {name}:")
            for key, value in people_info[name].items():
                print(f"  {key}: {value}")
        else:
            print(f"Name '{name}' Not Found. Please Try Another Name.")

# Run the program
main()
