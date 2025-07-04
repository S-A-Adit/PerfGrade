import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Download latest version
path = kagglehub.dataset_download("lainguyn123/student-performance-factors")
print("Path to dataset files:", path)

# Step 2: Load dataset
csv_path = os.path.join(path, "StudentPerformanceFactors.csv")
df = pd.read_csv(csv_path)

# Step 3: Numeric Summaries
numeric_summary = {
    "Average Exam Score": df['Exam_Score'].mean(),
    "Average Previous Scores": df['Previous_Scores'].mean(),
    "Average Hours Studied per Week": df['Hours_Studied'].mean(),
    "Average Tutoring Sessions per Month": df['Tutoring_Sessions'].mean(),
    "Average Sleep Hours per Night": df['Sleep_Hours'].mean(),
    "Average Physical Activity Hours per Week": df['Physical_Activity'].mean(),
    "Average Attendance Percentage": df['Attendance'].astype(float).mean()
}

# Step 4: Statement-Based Analysis (Grouped Mean Scores)
statement_output = {
    "Motivation_Level": df.groupby('Motivation_Level')['Exam_Score'].mean().to_dict(),
    "Internet_Access": df.groupby('Internet_Access')['Exam_Score'].mean().to_dict(),
    "Extracurricular_Activities": df.groupby('Extracurricular_Activities')['Exam_Score'].mean().to_dict(),
    "Parental_Education_Level": df.groupby('Parental_Education_Level')['Exam_Score'].mean().to_dict(),
    "School_Type": df.groupby('School_Type')['Exam_Score'].mean().to_dict(),
    "Learning_Disabilities": df.groupby('Learning_Disabilities')['Exam_Score'].mean().to_dict(),
    "Gender": df.groupby('Gender')['Exam_Score'].mean().to_dict(),
    "Distance_from_Home": df.groupby('Distance_from_Home')['Exam_Score'].mean().to_dict(),
    "Peer_Influence": df.groupby('Peer_Influence')['Exam_Score'].mean().to_dict(),
    "Access_to_Resources": df.groupby('Access_to_Resources')['Exam_Score'].mean().to_dict()
}


print("\n--- Numeric Summary ---")
for k, v in numeric_summary.items():
    print(f"{k}: {v:.2f}")

print("\n--- Statement Insights ---")
for category, values in statement_output.items():
    print(f"\n{category}:")
    for k, v in values.items():
        print(f"  {k}: {v:.2f}")
