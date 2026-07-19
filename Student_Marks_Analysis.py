# Student Marks Analysis System

import pandas as pd
import numpy as np

# Read Excel File
try:
    df = pd.read_excel("Student_Data.xlsx")
except FileNotFoundError:
    print("Error: Student_Data.xlsx file not found!")
    exit()

print("\n========== STUDENT DATA ==========")
print(df)

# Convert Marks column into NumPy Array
marks = np.array(df["Marks"])

# Display Statistics
print("\n========== STATISTICS ==========")
print(f"Total Students : {len(df)}")
print(f"Average Marks  : {np.mean(marks):.2f}")
print(f"Highest Marks  : {np.max(marks)}")
print(f"Lowest Marks   : {np.min(marks)}")
print(f"Total Marks    : {np.sum(marks)}")

# Grade Function
def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 35:
        return "D"
    else:
        return "F"

# Add Grade Column
df["Grade"] = df["Marks"].apply(calculate_grade)

# Add Pass/Fail Status
df["Status"] = np.where(df["Marks"] >= 35, "Pass", "Fail")

# Display Student Report
print("\n========== STUDENT REPORT ==========")
print(df)

# Topper
topper = df.loc[df["Marks"].idxmax()]

print("\n========== TOPPER ==========")
print(f"Name  : {topper['Name']}")
print(f"Marks : {topper['Marks']}")
print(f"Grade : {topper['Grade']}")

# Top 3 Students
print("\n========== TOP 3 STUDENTS ==========")
top3 = df.sort_values(by="Marks", ascending=False).head(3)
print(top3)

# Pass/Fail Count
pass_count = len(df[df["Status"] == "Pass"])
fail_count = len(df[df["Status"] == "Fail"])

print("\n========== RESULT SUMMARY ==========")
print(f"Pass Students : {pass_count}")
print(f"Fail Students : {fail_count}")

# Grade Distribution
print("\n========== GRADE DISTRIBUTION ==========")
print(df["Grade"].value_counts())

# Save Report to Excel
df.to_excel("Student_Report.xlsx", index=False)

print("\nStudent_Report.xlsx has been created successfully!")

print("\n========== THANK YOU ==========")
print("Student Marks Analysis Completed Successfully!")