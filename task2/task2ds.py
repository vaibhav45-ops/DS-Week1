"""
Task 2: Python Programming
Accept marks of 5 students, calculate average, display highest/lowest.
"""

def get_marks(num_students=5):
    marks = []
    for i in range(1, num_students + 1):
        while True:
            try:
                mark = float(input(f"Enter marks for Student {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter marks between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return marks


def analyze_marks(marks):
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    return average, highest, lowest


def main():
    print("=== Student Marks Analyzer ===\n")
    marks = get_marks(5)
    average, highest, lowest = analyze_marks(marks)

    print("\n--- Results ---")
    print(f"Marks Entered : {marks}")
    print(f"Average Marks : {average:.2f}")
    print(f"Highest Marks : {highest}")
    print(f"Lowest Marks  : {lowest}")


if __name__ == "__main__":
    main()