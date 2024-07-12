import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace this with your actual dataset)
df = pd.read_csv('survey.csv')


df.columns = ['timestamp','grade', 'subject', 'learning_pref', 'career', 'group_pref','difficulty', 'elective', 'email'] #switch email and elective after new data is here

#only include learning and group pref if they are mentioned first 
# and detected using nlp if not dont use them in features

#the more things the user writes about, the more likely
#that decision tree will be prioritized
#however the less the user uses the more 
# likely basic filtering will be prioritized
#however basic filtering should always be used

#basic filter will be based on nlp and using things other than
#the things mentioned in the survey such as subject difficulty 
# or foreign language
#however it will also include the things in the survey for accuracy

#also depends on how much information survey ends up collecting

#in the website if there isnt enuogh data given then the chat should ask
#for what nlp couldnt find like if they didnt mention a subject or smth

# Mapping categorical data to numerical data
learning_pref_map = {'Practical': 1,
                    'Theoretical': 0, 
                    'No preference': 2}
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


elective_map = {
    'AP English (Language or Literature) & Composition': 0,
    'AP Calculus (AB or BC)': 1,
    'AP Statistics': 1,
    'AP Biology': 2,
    'AP Chemistry': 14,
    'AP Physics (1, 2 or C)': 3,
    'AP Environmental Science': 2,
    'AP Psychology': 4,
    'AP US Government & Politics': 5,
    'AP Macroeconomics': 5,
    'AP Computer Science Principles': 6,
    'Adv. C.A.D. Civil Engineering & Architecture': 7,
    'Advanced Computer Applications & Development': 6,
    'Adv. AV Engineering & TV Studio (1 through 3)': 8,
    'Advanced Russian': 9,
    'Applied Physics': 3,
    'Behavioral & Social Science Class': 4,
    'Biotechnology': 2,
    'Creative Writing': 0,
    'Computer Science & Engineering': 6,
    'C.A.D / Civil Engineering & Architecture': 7,
    'Career Financial Management & Entrepreneurship': 10,
    'College Russian': 9,
    'Concert Bands': 11,
    'Chamber Music': 11,
    'Design & Fabrication (Makerspace)': 12,
    'Electronics & Green Technology': 13,
    'Forensic Science': 2,
    'Fundamentals of Engineering': 13,
    'Freshmen Band': 11,
    'Human Anatomy & Physiology': 2,
    'Intro to AV Engineering & TV Studio': 8,
    'Jazz Ensemble': 11,
    'Modern Mythology: Gods & Monsters': 0,
    'Multivariable Calculus': 1,
    'Marching Band': 11,
    'Publications': 0,
    'Public Speaking': 0,
    'Russian for Business': 9,
    'String Ensemble': 11,
    'Symphonic Band': 11,
    'Theater Production': 8,
    'Wind Ensemble': 11,
    'Work Based Learning (1 or 2)': 10,
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
    'Science': 1, 'Math': 2, 'Ela': 3, 
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
features = ['subject', 'career', 'group_pref']
target = 'elective'
#PLAY AROUND WITH THE FEATURES AND SEE WHAT WORKS BEST

X = df[features]
y = df[target]

p = [0, 1, 2, 3, 4, 5]

# Train the decision tree with priorities
dtree = DecisionTreeClassifier()
#dtree.priorities = p
dtree = dtree.fit(X, y)

reverse_elective_map = {}
for class_name, number in elective_map.items():
    if number in reverse_elective_map:
        reverse_elective_map[number].append(class_name)
    else:
        reverse_elective_map[number] = [class_name]
reverse_subject_map = {v: k for k, v in subject_map.items()}
reverse_career_map = {v: k for k, v in career_map.items()}
reverse_group_map = {v: k for k, v in group_pref_map.items()}
reverse_learning_map = {v: k for k, v in learning_pref_map.items()}


# Predict with the trained decision tree
predicted_classes = dtree.predict_proba(np.array([[5, 3, 2]]))[0]
top_n_indices = predicted_classes.argsort()[-3:][::-1]  # Top 3 classes
top_recommended_classes = [dtree.classes_[i] for i in top_n_indices]

groupResults = []

for course in top_recommended_classes:
    #print(elective_map[course])
    groupResults.append([c for c in reverse_elective_map[elective_map[course]]])

#filter out the group results based on the grade and other things that will be given using the nlp here

#map all the reverse maps
df['subject'] = df['subject'].map(reverse_subject_map)
df['career'] = df['career'].map(reverse_career_map)
df['group_pref'] = df['group_pref'].map(reverse_group_map)
df['learning_pref'] = df['learning_pref'].map(reverse_learning_map)

#print(df)
print("Top 3 Recommended Classes:", top_recommended_classes)

# Visualize the decision tree using matplotlib
plt.figure(figsize=(20,10), dpi=500)
plot_tree(dtree, feature_names=features, class_names=list(elective_map.keys()), filled=True, max_depth=5)
plt.savefig("decision_tree.png", bbox_inches="tight")  # Save to file

