import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace this with your actual dataset)
df = pd.read_csv('survey.csv')

# Mapping categorical data to numerical data
grade_map = {'9th': 0, '10th': 1, '11th': 2, '12th': 3}
df['grade'] = df['grade'].map(grade_map)

learning_pref_map = {'Practical': 1, 'Theoretical': 0}
df['learning_pref'] = df['learning_pref'].map(learning_pref_map)

career_map = {
    'Law': 0, 'Finance': 1, 'Medicine': 2, 'Software Development': 3, 
    'Teaching/Education': 4, 'Marketing': 5, 'Data Science': 6, 
    'Psychology': 7, 'Environmental Science': 8, 'Music Production': 9, 
    'Culinary Arts': 10, 'Engineering(Mechanical, Electrical, Civil, ect...)': 11, 
    'Graphic Design': 12, 'Movie/Show Production': 13
}

group_pref_map = {'Group': 0, 'Independent': 1, 'No preference': 2}
df['group_pref'] = df['group_pref'].map(group_pref_map)

#make electives lowercase
df['elective'] = df['elective'].str.lower()

elective_map = {'computer science': 0, 
                'graphic design': 1, 
                'marketing': 2, 
                'machine learning': 3,
                }
df['elective'] = df['elective'].map(elective_map)

# Expand rows for multiple careers
new_df = pd.DataFrame()
for index, row in df.iterrows():
    careers = row['career'].split(', ')
    for career in careers:
        new_row = row.copy()
        new_row['career'] = career_map[career.strip()]
        new_df = new_df._append(new_row, ignore_index=True)
df = new_df
print(df)

subject_map = {
    'Theoretical': 0, 'Science': 1, 'Math': 2, 'Ela': 3, 
    'Photography/Videography': 4, 'Robotics': 5, 'History': 6, 
    'Engineering': 7, 'Art': 8, 'Music': 9, 
    'Performing Arts': 10, 'Audio Visual (AV)': 11
}

# Expand rows for multiple subjects
new_df = pd.DataFrame()
for index, row in df.iterrows():
    subjects = row['subject'].split(', ')
    for subject in subjects:
        new_row = row.copy()
        new_row['subject'] = subject_map[subject.strip()]
        new_df = new_df._append(new_row, ignore_index=True)
df = new_df
print(df)

# Defining features and target
features = ['grade', 'subject', 'learning_pref', 'career', 'group_pref', 'difficulty']
target = 'elective'

X = df[features]
y = df[target]

# Train the decision tree
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

# Predict with the trained decision tree
predicted_classes = dtree.predict_proba(np.array([[0, 3, 0, 5, 0, 8]]))[0]
top_n_indices = predicted_classes.argsort()[-3:][::-1]  # Top 3 classes
top_recommended_classes = [dtree.classes_[i] for i in top_n_indices]
print("Top 3 Recommended Classes:", top_recommended_classes)

# Visualize the decision tree using matplotlib
plt.figure(figsize=(20,10))
plot_tree(dtree, feature_names=features, class_names=list(elective_map.keys()), filled=True)
plt.savefig("decision_tree.png")  # Save to file
plt.show()  # Display the plot

