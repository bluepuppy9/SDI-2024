import json
# Natural language processing example
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Load the data
with open('classes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def filter_classes(data, difficulty=None, grades=None, subject=None):
    filtered_classes = []
    print(difficulty, grades, subject)
    for category, details in data.items():
        for course in details:
            if difficulty is not None and course['difficulty'] != difficulty:
                continue
            if grades is not None and not any(grade in grades for grade in course['grades']):
                continue
            if subject is not None and course['subject'].lower() != subject:
                continue
            filtered_classes.append(course)

    return filtered_classes

#User preferences
#
## Filter classes
#filtered_classes = filter_classes(data, grades=user_preferences['grades'], subject=user_preferences['subject'])
#for cls in filtered_classes:
#    print(f'{cls["class"]}: {cls["description"]}')
#    print(f'Grades: {cls["grades"]}')
#    print(f'Difficulty: {cls["difficulty"]}')
#    print(f'Subject: {cls["subject"]}')


def extract_preferences(text):
    tokens = word_tokenize(text)
    filtered_tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    grades = [int(token) for token in lemmatized_tokens if token.isdigit()]
    subject = next((token for token in lemmatized_tokens if token.lower() in ['math', 'science', 'english', 'history']), None)
    return {'grades': grades, 'subject': subject}

example_text = input("Enter your preferences: ")
user_preferences = extract_preferences(example_text)
for item in user_preferences:
    if len(user_preferences[item]) < 1:
        user_preferences[item] = None
filtered_classes = filter_classes(data,grades=user_preferences['grades'], subject=user_preferences['subject'])
for cls in filtered_classes:
    print(f'{cls["class"]}: {cls["grades"]}', cls["difficulty"], cls["subject"])
