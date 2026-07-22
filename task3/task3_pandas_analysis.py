"""
Task 3: Data Analysis using Pandas
Reads students.csv, displays records, computes average marks,
and shows the top-scoring student.
"""

import pandas as pd

# Read the CSV file
df = pd.read_csv("students.csv")

# Display first 5 records
print("=== First 5 Records ===")
print(df.head())

# Calculate average marks
average_marks = df["Marks"].mean()
print(f"\nAverage Marks: {average_marks:.2f}")

# Student with highest marks
top_student = df.loc[df["Marks"].idxmax()]
print("\n=== Student with Highest Marks ===")
print(top_student)

# Display complete dataset
print("\n=== Complete Dataset ===")
print(df)