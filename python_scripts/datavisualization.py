import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import kagglehub

# Download and get the dataset folder path
path = kagglehub.dataset_download("lainguyn123/student-performance-factors")
print("Path to dataset files:", path)
# Now read the CSV file from the downloaded path
csv_path = os.path.join(path, "StudentPerformanceFactors.csv")  # Replace with actual filename
df = pd.read_csv(csv_path)


#Fig 1
plt.figure(figsize=(8, 6))

# Scatterplot with hue
sns.scatterplot(data=df, x='Hours_Studied', y='Exam_Score', hue='Gender')

# Add overall regression line
sns.regplot(data=df, x='Hours_Studied', y='Exam_Score',
            scatter=False, color='black', line_kws={"label": "Line of Best Fit"})

plt.title('Hours Studied vs Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

#Figure 2
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Motivation_Level', y='Previous_Scores', order=['Low', 'Medium', 'High'])
plt.title('Previous Score Distribution by Motivation Level')
plt.xlabel('Motivation Level')
plt.ylabel('Previous Score')
plt.grid(True)
plt.tight_layout()
plt.show()

#Figure 3
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Motivation_Level', hue='Gender', order=['Low', 'Medium', 'High'])
plt.title('Motivation Level Distribution by Gender')
plt.xlabel('Motivation Level')
plt.ylabel('Number of Students')
plt.grid(True)
plt.tight_layout()
plt.show()


#Figure 4
cross_tab = pd.crosstab(df['Extracurricular_Activities'], df['Peer_Influence'])

# Step 2: Ensure consistent column order
cross_tab = cross_tab[['Positive', 'Neutral', 'Negative']]

# Step 3: Plot stacked bar chart
colors = ['green', 'grey', 'red']
cross_tab.plot(kind='bar', stacked=True, color=colors, figsize=(8, 6))

# Step 4: Final touches
plt.title('Peer Influence by Participation in Extracurricular Activities')
plt.xlabel('Extracurricular Activities')
plt.ylabel('Number of Students')
plt.legend(title='Peer Influence')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#Figure 5
plt.figure(figsize=(8, 6))
sns.lineplot(data=df, x='Tutoring_Sessions', y='Previous_Scores', ci=None, marker='o', color='blue')
plt.title('Average Previous Scores vs Tutoring Sessions per Month')
plt.xlabel('Number of Tutoring Sessions')
plt.ylabel('Previous Exam Score')
plt.grid(True)
plt.tight_layout()
plt.show()
