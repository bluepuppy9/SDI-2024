#import json
## Natural language processing example
#import nltk
#from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
#from nltk.stem import WordNetLemmatizer
#
## Load the data
#with open('classes.json', 'r', encoding='utf-8') as f:
#    data = json.load(f)
#
#def filter_classes(data, difficulty=None, grades=None, subject=None):
#    filtered_classes = []
#    print(difficulty, grades, subject)
#    for category, details in data.items():
#        for course in details:
#            if difficulty is not None and course['difficulty'] != difficulty:
#                continue
#            if grades is not None and not any(grade in grades for grade in course['grades']):
#                continue
#            if subject is not None and not any(sub.lower() in course['subject'].lower() for sub in subject):
#                continue
#            filtered_classes.append(course)
#
#    return filtered_classes
#
##User preferences
##
### Filter classes
##filtered_classes = filter_classes(data, grades=user_preferences['grades'], subject=user_preferences['subject'])
##for cls in filtered_classes:
##    print(f'{cls["class"]}: {cls["description"]}')
##    print(f'Grades: {cls["grades"]}')
##    print(f'Difficulty: {cls["difficulty"]}')
##    print(f'Subject: {cls["subject"]}')
#
#
#def extract_preferences(text):
#    tokens = word_tokenize(text)
#    filtered_tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stopwords.words('english')]
#    lemmatizer = WordNetLemmatizer()
#    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
#    grades = [int(token) for token in tokens if token.isdigit()]
#    subject = [token for token in lemmatized_tokens if token.lower() in ['math', 'science', 'ela', 'history', 'russian', 'career and Technical', 'performing arts', 'physical education']]
#    return {'grades': grades, 'subject': subject}
#
#example_text = input("Enter your preferences: ")
#user_preferences = extract_preferences(example_text)
#for item in user_preferences:
#    if item=='grades':
#        if user_preferences[item] == []:
#            user_preferences[item] = None
#    if item=='subject':
#        if user_preferences[item] == []:
#            user_preferences[item] = None
#filtered_classes = filter_classes(data,grades=user_preferences['grades'], subject=user_preferences['subject'])
#for cls in filtered_classes:
#    print(f'{cls["class"]}: {cls["grades"]}', cls["difficulty"], cls["subject"])

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing

# create data
people = 10000
classes = 10
grades = ['9', '10', '11', '12']
difficulties = ['1', '2', '3', '4', '5']
fields = ['Math', 'Science', 'ELA', 'History', 'Russian', 'Career and Technical', 'Performing Arts', 'Physical Education']


data = pd.DataFrame({'Grade': np.random.choice(grades, size=people),
                     'Difficulty': np.random.choice(difficulties, size=people),
                     'Field': np.random.choice(fields, size=people),
                     'Accepted': np.random.choice([True, False], size=people)})

# preprocess categorical data
le = preprocessing.LabelEncoder()
data['Grade'] = le.fit_transform(data['Grade'])
data['Difficulty'] = le.fit_transform(data['Difficulty'])
data['Field'] = le.fit_transform(data['Field'])

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data[['Grade', 'Difficulty', 'Field']], data['Accepted'], test_size=0.2, random_state=42)

# create and train decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# make a prediction
prediction = clf.predict([[9, 3, 6]]) # someone in 10th grade who wants a class that is moderately hard and in the field of science

print(f'This person might want to apply to class {le.inverse_transform(prediction)[0] + 1}')
