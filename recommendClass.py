import pandas as pd
import joblib

# Load the decision tree model
clf = joblib.load('decision_tree_model.pkl')

# Load the feature names
feature_names = pd.read_csv('feature_names.csv').squeeze()

# Sample user input
new_user = {
    "grade_level": 10,
    "interests": ["science"],
    "hobbies": ["robotics", "coding"],
    "learning_preference": "practical",
    "project_preference": "individual",
    "ap_courses": True,
    "difficulty_tolerance": 4,
    "career_path": "Engineering",
    "languages": 1
}

# Convert the new user input to DataFrame
user_input = pd.DataFrame([new_user])

# Convert list columns to strings for encoding
user_input['interests'] = user_input['interests'].apply(lambda x: ','.join(x))

# Convert categorical data to numerical data
user_input['ap_courses'] = user_input['ap_courses'].astype(int)
user_input['learning_preference'] = user_input['learning_preference'].apply(lambda x: 1 if x == 'practical' else 0)
user_input['project_preference'] = user_input['project_preference'].apply(lambda x: 1 if x == 'individual' else 0)

# Dummy encoding for interests, career_path, and languages
user_input = pd.get_dummies(user_input, columns=['interests', 'career_path'], drop_first=True)

# Ensure all columns match the training data
for col in feature_names:
    if col not in user_input.columns:
        user_input[col] = 0

# Reorder the columns to match the training data
user_input = user_input[feature_names]

# Predict recommended classes
recommended_classes = clf.predict_proba(user_input)
top_recommended_classes = []
for probs in recommended_classes:
    top_n_indices = probs.argsort()[-3:][::-1]  # Top 5 classes
    top_recommended_classes.append([clf.classes_[i] for i in top_n_indices])

print("Top 5 Recommended Classes:", top_recommended_classes)
