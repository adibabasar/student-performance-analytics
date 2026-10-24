import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load student dataset
df = pd.read_csv("students.csv")

# Define subject columns
subjects = ["Python", "Mathematics", "Statistics"]

# Calculate total and average marks
df["Total_Marks"] = df[subjects].sum(axis=1)
df["Average_Marks"] = df[subjects].mean(axis=1)

# Assign grades
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average_Marks"].apply(calculate_grade)

# Assign pass/fail status
df["Result"] = np.where(
    df["Average_Marks"] >= 40, "Pass", "Fail"
)

# Display individual student results
print("\n===== STUDENT PERFORMANCE ANALYSIS =====")
display_columns = [
    "Name", "Total_Marks", "Average_Marks", "Grade", "Result"
]
print(df[display_columns].to_string(index=False))

# Class performance summary
print("\n===== CLASS PERFORMANCE SUMMARY =====")
print("Total Students:", len(df))
print("Class Average:", round(df["Average_Marks"].mean(), 2))
print("Highest Average:", round(df["Average_Marks"].max(), 2))
print("Lowest Average:", round(df["Average_Marks"].min(), 2))
print("Students Passed:", (df["Result"] == "Pass").sum())
print("Students Failed:", (df["Result"] == "Fail").sum())

# Top 5 students
print("\n===== TOP 5 STUDENTS =====")
print(
    df.nlargest(5, "Average_Marks")[
        ["Name", "Average_Marks", "Grade"]
    ].to_string(index=False)
)

# Subject-wise analysis
print("\n===== SUBJECT-WISE PERFORMANCE =====")
for subject in subjects:
    print("\nSubject:", subject)
    print("Class Average:", round(df[subject].mean(), 2))
    print("Highest Mark:", df[subject].max())
    print("Lowest Mark:", df[subject].min())

print(
    "\nBest Performing Subject:",
    df[subjects].mean().idxmax()
)

# Attendance analysis
print("\n===== ATTENDANCE ANALYSIS =====")
print("Class Average Attendance:",
      round(df["Attendance"].mean(), 2), "%")
print("\nStudents with attendance below 75%:")
print(
    df.loc[df["Attendance"] < 75, ["Name", "Attendance"]]
      .to_string(index=False)
)

# Save analyzed results
df.to_csv("student_analysis_results.csv", index=False)
print("\nAnalysis results saved to student_analysis_results.csv")

# Plot subject averages
averages = [df[subject].mean() for subject in subjects]
plt.figure(figsize=(8, 5))
plt.bar(subjects, averages)
plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("subject_performance.png")
plt.show()
