import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace this with your actual dataset)
df = pd.read_csv('survey.csv')


df.columns = ['timestamp','grade', 'subject', 'learning_pref', 'career', 'group_pref','difficulty', 'elective', 'email'] #switch email and elective after new data is here

# Mapping categorical data to numerical data
learning_pref_map = {'Practical': 1, 'Theoretical': 0, 'No preference': 2}
df['learning_pref'] = df['learning_pref'].map(learning_pref_map)

career_map = {
    'Law': 0, 'Finance': 1, 'Medicine': 2, 'Software Development': 3, 
    'Teaching/Education': 4, 'Marketing': 5, 'Data Science': 6, 
    'Psychology': 7, 'Environmental Science': 8, 'Music Production': 9, 
    'Culinary Arts': 10, 'Engineering': 11, 
    'Graphic Design': 12, 'Movie/Show Production': 13, "Entrepreneur": 14, 'Architecture ': 15
}

group_pref_map = {'Group': 0, 'Independent': 1, 'No preference': 2}
df['group_pref'] = df['group_pref'].map(group_pref_map)

#make electives lowercase
df['elective'] = df['elective'].str.lower()
df['elective'] = df['elective'].str.replace(' ', '')
elective_map = {
    'computerscience': 0,
    'band': 1,
    'av': 2,
    'buisness': 3,
    'physics c': 4,
    'engineering': 5,
    'art': 6,
    'robotics': 7,
    'apcompsci': 8,
    'fundamentalsofengineering': 9,
    'wind ensemble': 10,
    'apjava': 8,
    'apcompscijava': 8,
    'photoshop': 2,
    'elective12': 14,
    'elective13': 15,
    'elective14': 16,
    'elective15': 17,
    'elective16': 18,
    'elective17': 19
}
# Expand rows for multiple careers
new_df = pd.DataFrame()
for index, row in df.iterrows():
    careers = row['career'].split(', ')
    for career in careers:
        new_row = row.copy()
        new_row['career'] = career_map[career.strip()]
        new_df = new_df._append(new_row, ignore_index=True)
df = new_df

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

# Defining features and target
features = ['subject', 'learning_pref', 'career', 'group_pref', 'difficulty']
target = 'elective'

X = df[features]
y = df[target]

p = [0, 1, 2, 3, 4, 5]

# Train the decision tree with priorities
dtree = DecisionTreeClassifier()
dtree.priorities = p
dtree = dtree.fit(X, y)

reverse_elective_map = {v: k for k, v in elective_map.items()}
reverse_subject_map = {v: k for k, v in subject_map.items()}
reverse_career_map = {v: k for k, v in career_map.items()}
reverse_group_map = {v: k for k, v in group_pref_map.items()}
reverse_learning_map = {v: k for k, v in learning_pref_map.items()}


# Predict with the trained decision tree
predicted_classes = dtree.predict_proba(np.array([[0, 0, 0, 5, 0]]))[0]
top_n_indices = predicted_classes.argsort()[-3:][::-1]  # Top 3 classes
top_recommended_classes = [reverse_elective_map[dtree.classes_[i]] for i in top_n_indices]

#map all the reverse maps
df['elective'] = df['elective'].map(reverse_elective_map)
df['subject'] = df['subject'].map(reverse_subject_map)
df['career'] = df['career'].map(reverse_career_map)
df['group_pref'] = df['group_pref'].map(reverse_group_map)
df['learning_pref'] = df['learning_pref'].map(reverse_learning_map)

print(df)
print("Top 3 Recommended Classes:", top_recommended_classes)

# Visualize the decision tree using matplotlib
plt.figure(figsize=(20,10))
plot_tree(dtree, feature_names=features, class_names=list(elective_map.keys()), filled=True)
plt.savefig("decision_tree.png")  # Save to file
plt.show()  # Display the plot


