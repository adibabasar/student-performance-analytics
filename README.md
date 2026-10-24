# Student Performance Analytics System

## Project Overview
The Student Performance Analytics System is a Python-based mini project that analyzes student academic performance using marks and attendance data. It calculates total marks, average marks, grades, pass/fail status, and subject-wise performance.

## Objectives
- Analyze student marks using Python.
- Calculate total and average marks.
- Assign grades and pass/fail status.
- Identify the top 5 performing students.
- Analyze subject-wise performance.
- Identify students with low attendance.
- Visualize subject averages using a bar chart.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Google Colab
- GitHub

## Project Files
- `main.py` – Main Python program.
- `Student_performance_analysis.ipynb` – Google Colab notebook containing code and outputs.
- `students.csv` – Original student dataset.
- `student_analysis_results.csv` – Analyzed student data with totals, averages, grades, and results.

## Features
1. Student marks analysis.
2. Grade calculation.
3. Pass/fail classification.
4. Class performance summary.
5. Top 5 student identification.
6. Subject-wise statistics.
7. Attendance analysis.
8. Bar chart visualization.
9. Export of analyzed results to CSV.

## How to Run
1. Install Python.
2. Install the required libraries:

   `pip install pandas numpy matplotlib`

3. Keep `main.py` and `students.csv` in the same folder.
4. Run the program:

   `python main.py`

5. The program displays the analysis, saves `student_analysis_results.csv`, and generates `subject_performance.png`.

## Sample Results
The current dataset contains 20 students.

- Class average marks: 70.58
- Highest student average: 95.67
- Lowest student average: 34.33
- Students passed: 19
- Students failed: 1
- Best-performing subject: Statistics
- Class average attendance: 81%

## Conclusion
This project demonstrates how Python libraries can be used to analyze student performance, summarize academic results, identify attendance concerns, and visualize data.
