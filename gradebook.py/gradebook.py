

#` ------------------------------------------------------------
# Title   : GradeBook Analyzer
# Author  : HIMANSHI
# Date    : 05-Nov-2025
# Purpose : Analyze and Report Student Grades using Python
# ------------------------------------------------------------

import csv
import statistics

# ------------------------------------------------------------
# Task 1: Welcome Message and Menu
# ------------------------------------------------------------
def show_menu():
    print("\n===== GRADEBOOK ANALYZER =====")
    print("1. Enter student data manually")
    print("2. Load data from CSV file")
    print("3. View sample demo (auto data)")
    print("4. Exit")
    print("==============================")

# ------------------------------------------------------------
# Task 2: Data Entry or CSV Import
# ------------------------------------------------------------
def manual_entry():
    marks = {}
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        score = float(input(f"Enter marks of {name}: "))
        marks[name] = score
    return marks

def load_from_csv(filename):
    marks = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                marks[row['Name']] = float(row['Marks'])
        print("CSV file loaded successfully ✅")
    except FileNotFoundError:
        print("❌ CSV file not found. Please check the filename.")
    return marks

def sample_data():
    return {
        "Honey": 95,
        "Babita": 50,
        "Chirag": 60,
        "Deepika": 67,
        "mohit": 75,
        "Firoj": 36,
        "Reena": 81,
    }

# ------------------------------------------------------------
# Task 3: Statistical Analysis
# ------------------------------------------------------------
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    max_student = max(marks_dict, key=marks_dict.get)
    return max_student, marks_dict[max_student]

def find_min_score(marks_dict):
    min_student = min(marks_dict, key=marks_dict.get)
    return min_student, marks_dict[min_student]

# ------------------------------------------------------------
# Task 4: Grade Assignment
# ------------------------------------------------------------
def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

def grade_distribution(grades):
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades.values():
        dist[g] += 1
    return dist

# ------------------------------------------------------------
# Task 5: Pass/Fail Filter (List Comprehension)
# ------------------------------------------------------------
def pass_fail_list(marks_dict):
    passed = [name for name, score in marks_dict.items() if score >= 40]
    failed = [name for name, score in marks_dict.items() if score < 40]
    return passed, failed

# ------------------------------------------------------------
# Task 6: Display Results Table
# ------------------------------------------------------------
def display_table(marks_dict, grades):
    print("\n-------------------------------------------")
    print("Name\t\tMarks\tGrade")
    print("-------------------------------------------")
    for name in marks_dict:
        print(f"{name:<15}{marks_dict[name]:<10}{grades[name]}")
    print("-------------------------------------------")

def export_to_csv(marks_dict, grades):
    with open("final_gradebook.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Marks", "Grade"])
        for name in marks_dict:
            writer.writerow([name, marks_dict[name], grades[name]])
    print("✅ Results exported to 'final_gradebook.csv'")

# ------------------------------------------------------------
# Main Program Loop
# ------------------------------------------------------------
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            marks = manual_entry()
        elif choice == "2":
            filename = input("Enter CSV file name (students.csv): ")
            marks = load_from_csv(filename)
        elif choice == "3":
            marks = sample_data()
            print("Loaded sample demo data ✅")
        elif choice == "4":
            print("Exiting... Goodbye,  HIMANSHI")
            break
        else:
            print("❌ Invalid choice, please try again.")
            continue

        if not marks:
            print("No data available!")
            continue

        # Perform analysis
        avg = calculate_average(marks)
        med = calculate_median(marks)
        high_name, high_score = find_max_score(marks)
        low_name, low_score = find_min_score(marks)

        print("\n📊 STATISTICAL SUMMARY 📊")
        print(f"Average Marks : {avg:.2f}")
        print(f"Median Marks  : {med:.2f}")
        print(f"Highest Score : {high_name} ({high_score})")
        print(f"Lowest Score  : {low_name} ({low_score})")

        # Assign grades
        grades = assign_grades(marks)
        dist = grade_distribution(grades)
        print("\n📘 GRADE DISTRIBUTION")
        for grade, count in dist.items():
            print(f"{grade}: {count}", end="\t")
        print()

        # Pass/Fail
        passed, failed = pass_fail_list(marks)
        print(f"\n✅ Passed Students: {', '.join(passed)}")
        print(f"❌ Failed Students: {', '.join(failed)}")

        # Display Table
        display_table(marks, grades)

        # Export
        export = input("\nDo you want to export results to CSV? (y/n): ")
        if export.lower() == "y":
            export_to_csv(marks, grades)

# ------------------------------------------------------------
# Run the program
# ------------------------------------------------------------
if __name__ == "__main__":
    main()