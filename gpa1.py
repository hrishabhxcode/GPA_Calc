print("CGPA_Calculator for National Institute of Technology Nagaland")


print("Select an option to proceed:\n"
      "a) GPA Calculator\n"
      "b) CGPA Calculator")


def get_gpa(grade):
    grade_to_gpa = {
        'S': 10,
        'A': 9,
        'B': 8,
        'C': 7,
        'D': 6,
        'E': 5,
        'U': 0,
        'I': 0,
        'W': 0
    }
    return grade_to_gpa.get(grade.upper(), 0)


def calc_gpa(total_points, total_credits):
    if total_credits!=0:
     return (total_points / total_credits)
    else:
        0




option = input("Enter the Choice: ")

if option == "a":
    print("The Score vs GPA are as follows:\n"
          "S  =>  10\n"
          "A  =>  09\n"
          "B  =>  08\n"
          "C  =>  07\n"
          "D  =>  06\n"
          "E  =>  05\n"
          "U  =>  00\n"
          "I  =>  00\n"
          "W  =>  00\n")

    courses = int(input("Enter the Number of Courses: "))

    total_quality_points = 0
    total_credits = 0

    for _ in range(courses):
        grade = input("Enter the Grade: ")
        credit = int(input("Enter the Credit: "))

        gpa = get_gpa(grade)
        total_quality_points += gpa * credit
        total_credits += credit

    final_gpa = calc_gpa(total_quality_points, total_credits)
    print(f"Your GPA is: {final_gpa:.2f}")


    if final_gpa==10:
        print("You have topped")
    elif final_gpa==9:
        print("Good Performance")

elif option == "b":
    print("CGPA Calculator is not yet implemented.")

    no_of_sem = int(input("Enter the Number of Semester :"))

    for i in range(1,no_of_sem+1):
        print(("Enter the Marks of Semester ",i ))

        gpa = int(input("Enter : "))

else:
    print("Invalid option selected.")




print("This Program is developed by StellarCosm")


input()
