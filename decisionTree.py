import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np
import re
from typing import List, Dict
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from nltk import ngrams
import csv

#if some things need to be donwloaded then just go to the download and put in the whole thing as a list so it can run from the servers

def check_class_subject(text: str, subjects: List[Dict[str, List[str]]]) -> List[str]:
    found_subjects = []
    for subject in subjects:
        for keyword in subject['keywords']:
            if re.search(rf'\b{re.escape(keyword)}\b', text, re.IGNORECASE):
                found_subjects.append(subject['name'])
                break
    return found_subjects if found_subjects else 'unknown'

def check_difficulty(text: str) -> str:
    difficulty_keywords = {
        'easy': ['easi', 'not hard', 'simpl'],
        'medium': ['medium', 'moder', 'not that hard', 'intermedi'],
        'hard': ['hard', 'difficult', 'challeng'],
    }
    normalized_text = text.lower()
    tokens = word_tokenize(normalized_text)
    
    # Generate trigrams
    trigrams = list(ngrams(tokens, 4))

    # Check for negation in trigrams
    for trigram in trigrams:
        if "not" in trigram or "don't" in trigram or "didn't" in trigram or "isn't" in trigram or "aren't" in trigram or "isnt" in trigram or "not" in trigram:
            for level, keywords in difficulty_keywords.items():
                for keyword in keywords:
                    if re.search(rf'\b{re.escape(keyword)}\b', normalized_text):
                        return [5, 6, 7]

    # Check for difficulty levels
    for level, keywords in difficulty_keywords.items():
        for keyword in keywords:
            if re.search(rf'\b{re.escape(keyword)}\b', normalized_text):
                if level == 'easy':
                    return [1, 2, 3, 4]
                elif level == 'medium':
                    return [4, 5, 6, 7]
                else:
                    return [7, 8, 9, 10]
                
    return "unknown"

def check_grade(text: str) -> str:
    grade_pattern = re.compile(r'\b(9th|10th|11th|12th|freshman|sophomore|junior|senior|freshmen|sophomores|juniors|seniors|sophmor|sophomor)\b', re.IGNORECASE)
    match = grade_pattern.search(text)
    if match is None:
        return "unknown"
    #map all the grades to 9th 10th 11th or 12th
    if match.group(0).lower() == "freshman":
        return "9th"
    elif match.group(0).lower() == "sophomore":
        return "10th"
    elif match.group(0).lower() == "junior":
        return "11th"
    elif match.group(0).lower() == "senior":
        return "12th"
    elif match.group(0).lower() == "freshmen":
        return "9th"
    elif match.group(0).lower() == "sophmor":
        return "10th"
    elif match.group(0).lower() == "sophomor":
        return "10th"
    return match.group(0).lower() if match else "unknown"

def check_career_path(text: str) -> List[str]:
    career_keywords = {
    "Law": ["law", "lawyer", "attorney", "legal"],
    "Finance": ["financ", "bank", "account", "economic"],
    "Medicine": ["medicine", "doctor", "physician", "medic", "health"],
    "Software Development": ["software", "develop", "program", "code", "programmer", "code", "engin", "comput"],
    "Teaching/Education": ["teach", "educate", "educator", "professor", "teachr", "educater", "professor"],
    "Marketing": ["market", "advertise", "brand", "promote"],
    "Data Science": ["data", "analyt", "comput"],
    "Psychology": ["psychology", "psychologist", "therapist", "counsel"],
    "Environmental Science": ["environ", "ecology", "conserve", 'biolog', 'environment'],
    "Music Production": ["music", "produce", "audio", "produc", "Product", "produced"],
    "Culinary Arts": ["culinary", "chef", "cook", "cuisine"],
    "Graphic Design": ["design", "graphic"],
    "Movie/Show Production": ["movie", "show", "film", "cinema", "television", "video"],
    "Entrepreneur": ["entrepreneur", "entrepreneur", "startup", "enterprise"],
    "Architecture": ["architectur", "architect", "building"]
}
    found_careers = []
    for career, keywords in career_keywords.items():
        for keyword in keywords:
            if re.search(rf'\b{re.escape(keyword)}\b', text, re.IGNORECASE):
                found_careers.append(career)
                #break
    return found_careers if found_careers else 'unknown'

def check_class (text: str, subjects: List[Dict[str, List[str]]]) -> List[str]:
    found_subjects = []
    for subject in subjects:
        for keyword in subject['keywords']:
            if re.search(rf'\b{re.escape(keyword)}\b', text, re.IGNORECASE):
                found_subjects.append(subject['name'])
                break
    return found_subjects if found_subjects else 'unknown'

def check_group_work(text: str) -> str:
    group_keywords = ['group', 'team', 'collab', 'together', 'collabor']
    not_group_keywords = ['alone', 'individual', 'single', 'by myself']
    normalized_text = text.lower()
    tokens = word_tokenize(normalized_text)
    
    # Generate trigrams
    trigrams = list(ngrams(tokens, 4))

    # Check for negation in trigrams
    for trigram in trigrams:
        if "not" in trigram or "don't" in trigram or "didn't" in trigram or "isn't" in trigram or "aren't" in trigram or "isnt" in trigram or "not" in trigram:
            for keywords in group_keywords:
                for keyword in keywords:
                    if re.search(rf'\b{re.escape(keyword)}\b', normalized_text):
                        return "Independent"

    # Check for difficulty levels
    for level in group_keywords:
        for keyword in level:
            if re.search(rf'\b{re.escape(keyword)}\b', normalized_text):
                return "Group"
    for level in not_group_keywords:
        for keyword in level:
            if re.search(rf'\b{re.escape(keyword)}\b', normalized_text):
                return "Independent"
                
    return "unknown"

# Example subjects list with keywords and abbreviations

# Example input text
classes =[
    {"name": "AP English (Language or Literature) & Composition", "keywords": ["English", "Lang", "Lit"]},
    {"name": "AP Calculus (AB or BC)", "keywords": ["Calculus", "Calc"]},
    {"name": "AP Statistics", "keywords": ["Stat"]},
    {"name": "AP Biology", "keywords": ["Bio", "Biology", "biolog"]},
    {"name": "AP Chemistry", "keywords": ["Chem"]},
    {"name": "AP Physics (1, 2 or C)", "keywords": ["Physics"]},
    {"name": "AP Environmental Science", "keywords": ["Environmental", "ecology", "conserve", 'biolog', 'environment', 'ecolog']},
    {"name": "AP Psychology", "keywords": ["Psych"]},
    {"name": "AP US Government & Politics", "keywords": ["US", "Gov", "GovPol"]},
    {"name": "AP Macroeconomics", "keywords": ["Macro"]},
    {"name": "AP Computer Science Principles", "keywords": ["Comp", "Sci", "Comput", "code"]},
    {"name": "Adv. C.A.D. Civil Engineering & Architecture", "keywords": ["CAD", "Civil","Architectur"]},
    {"name": "Advanced Computer Applications & Development", "keywords": ["Computer", "Applications", "Development"]},
    {"name": "Adv. AV Engineering & TV Studio (1 through 3)", "keywords": ["AV", "Engineering", "TV", "Studio", "video"]},
    {"name": "Advanced Russian", "keywords": ["Russian"]},
    {"name": "Applied Physics", "keywords": ["Applied", "Physics"]},
    {"name": "Behavioral & Social Science Class", "keywords": ["Behavioral", "Social"]},
    {"name": "Biotechnology", "keywords": ["Biotech"]},
    {"name": "Creative Writing", "keywords": ["Creative", "Writing"]},
    {"name": "C.A.D / Civil Engineering & Architecture", "keywords": ["CAD", "Civil","Architectur"]},
    {"name": "Career Financial Management & Entrepreneurship", "keywords": ["Financial", "Management", "Entrepreneur"]},
    {"name": "College Russian", "keywords": ["College", "Russian"]},
    {"name": "Concert Bands", "keywords": ["Concert", "Band"]},
    {"name": "Chamber Music", "keywords": ["Chamber", "Music"]},
    {"name": "Design & Fabrication (Makerspace)", "keywords": ["Design", "Fabrication", "Makerspace"]},
    {"name": "Electronics & Green Technology", "keywords": ["Electronics", "Green", "Technology"]},
    {"name": "Forensic Science", "keywords": ["Forensic"]},
    {"name": "Fundamentals of Engineering", "keywords": ["Fundamental", "Engin"]},
    {"name": "Freshmen Band", "keywords": ["Freshmen", "Band"]},
    {"name": "Human Anatomy & Physiology", "keywords": ["Human", "Anatomy", "Physiology"]},
    {"name": "Intro to AV Engineering & TV Studio", "keywords": ["Intro", "AV", "Engineering", "TV", "Studio"]},
    {"name": "Jazz Ensemble", "keywords": ["Jazz", "Ensembl"]},
    {"name": "Modern Mythology: Gods & Monsters", "keywords": ["Modern", "Mythology", "Gods", "Monsters"]},
    {"name": "Multivariable Calculus", "keywords": ["Multivariable", "Calculus"]},
    {"name": "Marching Band", "keywords": ["Marching", "Band"]},
    {"name": "Publications", "keywords": ["Publication"]},
    {"name": "Public Speaking", "keywords": ["Public", "Speaking"]},
    {"name": "Russian for Business", "keywords": ["Russian", "Busi"]},
    {"name": "String Ensemble", "keywords": ["String", "Ensembl"]},
    {"name": "Symphonic Band", "keywords": ["Symphonic", "Band"]},
    {"name": "Theater Production", "keywords": ["Theater", "Production"]},
    {"name": "Wind Ensemble", "keywords": ["Wind", "Ensembl", "Band"]},
    {"name": "Work Based Learning (1 or 2)", "keywords": ["Work Based", "Learning", "Learn"]},
]


subjects = [
    {"name": "Science", "keywords": ["scienc", "biolog", "chemistr", "physic", "environment", "forensic", "biotech", "anatom"]},
    {"name": "Math", "keywords": ["math", "mathemat", "calcul", "algebr", "statist", "geometr", "multivariable", "data"]},
    {"name": "Ela", "keywords": ["english", "ela", "literatur", "composit", "creativ", "public", "public", "mytholog"]},
    {"name": "Photography/Videography", "keywords": ["photograph", "videograph", "film", "tv"]},
    {"name": "Robotics", "keywords": ["robotic"]},
    {"name": "History", "keywords": ["history", "govern", "polit", "macro", "histori"]},
    {"name": "Art", "keywords": ["art", "draw", "paint", "sculptur", "fashion", "design"]},
    {"name": "Music", "keywords": ["music", "band", "orchestr", "ensembl", "jazz", "march", "wind"]},
    {"name": "Performing Arts", "keywords": ["theater", "product", "dance", "perform"]},
    {"name": "Audio Visual (AV)", "keywords": ["audio", "av", "video", "film", "tv"]},
    {"name": "Architecture", "keywords": ["architecture", "urban", "design", "cad", "civil", "architect"]},
]
text = input("Input: ")
stop_words = set(stopwords.words('english'))
stop_words.remove("not")    #get rid of "not" stop word from stop words
def preprocess(text):
    text = word_tokenize(text)
    #stem the words
    stemmer = SnowballStemmer("english")
    text = ' '.join([stemmer.stem(word) for word in text if word not in stop_words])
    text = text.lower()
    print(text)
    return text

text = preprocess(text)
found_subjects = check_class_subject(text, subjects)
difficulty_level = check_difficulty(text)
grade_level = check_grade(text)
career_path = check_career_path(text)
group_work_preference = check_group_work(text)
classes_found = check_class(text, classes)
while 'unknown' in [found_subjects, difficulty_level, grade_level, career_path]:
    while found_subjects == 'unknown':
        print(f"Please provide more information about any subjects you like.")
        text = input("Input: ")
        text = preprocess(text)
        found_subjects = check_class_subject(text, subjects)
        classes_found = check_class(text, classes)
    #while difficulty_level == 'unknown':
    #    print(f"Please provide more information about your difficulty level.")
    #    text = input("Input: ")
    #    text = preprocess(text)
    #    difficulty_level = check_difficulty(text)
    #while grade_level == '':
    #    print(f"Please provide more information about your grade level.")
    #    text = input("Input: ")
    #    text = preprocess(text)
    #    grade_level = check_grade(text)
    while career_path == 'unknown':
        print(f"Please provide more information about your career path.")
        text = input("Input: ")
        text = preprocess(text)
        career_path = check_career_path(text)
    #while group_work_preference == 'unknown':
    #    print(f"Please provide more information about your group work preference.")
    #    text = input("Input: ")
    #    text = preprocess(text)
    #    group_work_preference = check_group_work(text)
    #while classes_found == 'unknown':
    #    print(f"Please provide more information about any classes you like.")
    #    text = input("Input: ")
    #    text = preprocess(text)
    #    classes_found = check_class(text, classes)
# Print the results
print("Found Subjects:", found_subjects)
print("Difficulty Level:", difficulty_level)
print("Grade Level:", grade_level)
print("Career Path:", career_path)
print("Group Work Preference:", group_work_preference)
print("Classes Found:", classes_found)

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
    'Work Based Learning 1': 10,
    'Work Based Learning 2': 10,
    'Adv. AV Engineering & TV Studio 1': 8,
    'Adv. AV Engineering & TV Studio 2': 8,
    'Adv. AV Engineering & TV Studio 3': 8,
    'AP Physics 1': 3,
    'AP Physics 2': 3,
    'AP Physics C': 3,
    'AP Calculus AB': 1,
    'AP Calculus BC': 1,
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
    'Performing Arts': 10, 'Audio Visual (AV)': 11, "Architecture": 12
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

features = ['subject', 'career']

#if difficulty_level != "unknown":
 #   features.append('difficulty')
if group_work_preference != "unknown":
    features.append('group_pref')


# Defining features and target
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
for subject in found_subjects:
    for career in career_path:
        x = [subject_map[subject], career_map[career]]
        if 'group_pref' in features:
            x.append(group_pref_map[group_work_preference])
        predicted_classes = dtree.predict_proba(np.array([x]))[0]
        top_n_indices = predicted_classes.argsort()[-3:][::-1]  # Top 3 classes
        top_recommended_classes = [dtree.classes_[i] for i in top_n_indices]

        groupResults = []

        for course in top_recommended_classes:
            #print(elective_map[course])
            try:
                groupResults.append([c for c in reverse_elective_map[elective_map[course]]])
            except:
                pass

#BASIC FILTERING
print("Results from decision tree:",groupResults)

# Load the data with UTF-8 encoding
with open('classesTech.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

# Example user preferences
user_preferences = {
    'grades': grade_level if grade_level != "" else [],
    'subject': found_subjects,
    'difficulty': difficulty_level if difficulty_level != "" and difficulty_level != "unknown" else [],
}

def recommend_classes(preferences, data):
    recommended_classes = []

    for course in data:
        course_name = course['class']
        course_subject = course['subject']
        if course_subject in preferences['subject']:
            recommended_classes.append(course_name)
    return recommended_classes

# Call the recommend_classes function
groupResults.append(recommend_classes(user_preferences, data))

#add any classes directly stated in message
if classes_found != "unknown":
    for item in classes_found:
        groupResults.append(reverse_elective_map[elective_map[item]])
    #this may create duplicates in groupresults which will be looked for as an indicater of a good class

grade_to_class = {
    'AP English Language & Composition': [11],
    'AP English Literature & Composition': [12],
    'Modern Mythology: Gods & Monsters': [12],
    'Creative Writing': [12],
    'Publications': [12],
    'Public Speaking': [12],
    'AP Calculus AB': [12],
    'AP Calculus BC': [11, 12],
    'AP Statistics': [12],
    'Multivariable Calculus': [12],
    'AP Biology': [11, 12],
    'AP Chemistry': [11, 12],
    'AP Physics 1': [10, 11, 12],
    'AP Physics 2': [11, 12],
    'AP Physics C: Electricity and Magnetism': [12],
    'AP Physics C': [12],
    'AP Environmental Science': [11, 12],
    'AP Psychology': [11, 12],
    'Forensic Science': [11, 12],
    'Biotechnology': [12],
    'Human Anatomy & Physiology': [12],
    'Applied Physics': [11, 12],
    'Physics In Medicine': [10],
    'AP US Government & Politics': [12],
    'AP Macroeconomics': [12],
    'Behavioral & Social Science Class': [11, 12],
    'Intro to AV Engineering & TV Studio': [9],
    'Computer Science & Engineering': [9],
    'C.A.D. / Civil Engineering & Architecture': [10, 11],
    'Electronics & Green Technology': [10, 11, 12],
    'Adv. C.A.D. Civil Engineering & Architecture': [11, 12],
    'Fundamentals of Engineering': [11, 12],
    'Design & Fabrication (Makerspace)': [10, 11, 12],
    'AP Computer Science Principles': [10, 11, 12],
    'Advanced Computer Applications & Development': [11, 12],
    'Adv. AV Engineering & TV Studio 1': [10, 11, 12],
    'Adv. AV Engineering & TV Studio 2/3': [11, 12],
    'Career Financial Management & Entrepreneurship': [10, 11, 12],
    'Work Based Learning 1': [11, 12],
    'Work Based Learning 2': [12],
    'Advanced Russian': [10, 11],
    'College Russian': [12],
    'Russian for Business': [12],
    'Freshmen Band': [9],
    'Concert Bands': [10],
    'Symphonic Band': [11, 12],
    'Wind Ensemble': [10, 11, 12],
    'Jazz Ensemble': [9, 10, 11, 12],
    'String Ensemble': [9, 10, 11, 12],
    'Marching Band': [10, 11, 12],
    'Chamber Music': [9, 10, 11, 12],
    'Theater Production': [11, 12],
    'Fitness': [10, 11, 12],
    'Basketball': [10, 11, 12],
    'Badminton': [10, 11, 12],
    'Dance': [10, 11, 12],
    'Table Tennis': [10, 11, 12],
    'Volleyball': [10, 11, 12],
    'Volleyball Advanced': [10, 11, 12],
    'Weight Training': [10, 11, 12],
    'Team Physical Education': [10, 11, 12],
    'AP Calculus (AB or BC)': [0],
    'AP Physics (1, 2 or C)': [0],
    'Adv. AV Engineering & TV Studio (1 through 3)': [0],
    'Adv. AV Engineering & TV Studio 1': [10, 11, 12],
    'Adv. AV Engineering & TV Studio 2': [11, 12],
    'Adv. AV Engineering & TV Studio 3': [11, 12],
    'Adv. AV Engineering & TV Studio 2/3': [11, 12],
    'Work Based Learning (1 or 2)': [0],
}

classes_to_difficulty = {
    'AP English Language & Composition': [7, 8, 9, 10],
    'AP English Literature & Composition': [7, 8, 9, 10],
    'Modern Mythology: Gods & Monsters': [4, 5, 6, 7],
    'Creative Writing': [3, 4, 5, 6],
    'Publications': [5, 6, 7, 8],
    'Public Speaking': [4, 5, 6, 7],
    'AP Calculus AB': [8, 9, 10, 10],
    'AP Calculus BC': [8, 9, 10, 10],
    'AP Statistics': [7, 8, 9, 10],
    'Multivariable Calculus': [8, 9, 10, 10],
    'AP Biology': [7, 8, 9, 10],
    'AP Chemistry': [7, 8, 9, 10],
    'AP Physics 1': [6, 7, 8, 9],
    'AP Physics 2': [7, 8, 9, 10],
    'AP Physics C: Electricity and Magnetism': [8, 9, 10, 10],
    'AP Environmental Science': [6, 7, 8, 9],
    'AP Psychology': [5, 6, 7, 8],
    'Forensic Science': [4, 5, 6, 7],
    'Biotechnology': [5, 6, 7, 8],
    'Human Anatomy & Physiology': [6, 7, 8, 9],
    'Applied Physics': [5, 6, 7, 8],
    'Physics In Medicine': [5, 6, 7, 8],
    'AP US Government & Politics': [6, 7, 8, 9],
    'AP Macroeconomics': [6, 7, 8, 9],
    'Behavioral & Social Science Class': [5, 6, 7, 8],
    'Intro to AV Engineering & TV Studio': [2, 3, 4, 5],
    'Computer Science & Engineering': [3, 4, 5, 6],
    'C.A.D. / Civil Engineering & Architecture': [4, 5, 6, 7],
    'Electronics & Green Technology': [5, 6, 7, 8],
    'Adv. C.A.D. Civil Engineering & Architecture': [6, 7, 8, 9],
    'Fundamentals of Engineering': [5, 6, 7, 8],
    'Design & Fabrication (Makerspace)': [4, 5, 6, 7],
    'AP Computer Science Principles': [6, 7, 8, 9],
    'Advanced Computer Applications & Development': [6, 7, 8, 9],
    'Adv. AV Engineering & TV Studio 1': [5, 6, 7, 8],
    'Adv. AV Engineering & TV Studio 2/3': [6, 7, 8, 9],
    'Career Financial Management & Entrepreneurship': [4, 5, 6, 7],
    'Work Based Learning 1': [5, 6, 7, 8],
    'Work Based Learning 2': [5, 6, 7, 8],
    'Advanced Russian': [6, 7, 8, 9],
    'College Russian': [6, 7, 8, 9],
    'Russian for Business': [5, 6, 7, 8],
    'Freshmen Band': [2, 3, 4, 5],
    'Concert Bands': [3, 4, 5, 6],
    'Symphonic Band': [4, 5, 6, 7],
    'Wind Ensemble': [5, 6, 7, 8],
    'Jazz Ensemble': [4, 5, 6, 7],
    'String Ensemble': [3, 4, 5, 6],
    'Marching Band': [4, 5, 6, 7],
    'Chamber Music': [3, 4, 5, 6],
    'Theater Production': [5, 6, 7, 8],
}


#this peice of code runs at the end for more accuracy
if user_preferences['grades'] != '':
    if user_preferences['grades'] == '9th':
        user_preferences['grades'] = 9
    elif user_preferences['grades'] == '10th':
        user_preferences['grades'] = 10
    elif user_preferences['grades'] == '11th':
        user_preferences['grades'] = 11
    elif user_preferences['grades'] == '12th':
        user_preferences['grades'] = 12
    #check all items in groupResults for the grade level and filter out the ones that don't match by checking rows in classesTech
    postFinalResults = []
    for item in groupResults:
        for course in item:
            try:
                if user_preferences['grades'] != []:
                    if user_preferences['grades'] in grade_to_class[course]:
                        postFinalResults.append(course)
                    else:
                        print(f'Removed {course} from results')
                        pass
                else:
                    postFinalResults.append(course)
            except:
                pass

#get rid of duplicates in group results and get count of results
strongly_suggested = []
Final_results = []
for course in postFinalResults:
    if postFinalResults.count(course) > 1:
        strongly_suggested.append(course) if course not in strongly_suggested else None
    else:
        Final_results.append(course) if course not in Final_results and course not in strongly_suggested else None

#get the top 5 most popular classes
most_popular = sorted(strongly_suggested, key=strongly_suggested.count, reverse=True)[0:5]
for item in most_popular:
    if item in strongly_suggested:
        strongly_suggested.remove(item)

#filters through most suggested and strongly suggested and if difficluty is not matched removes
#if removed from most suggested or strongly suggested, item will be added to final results
if user_preferences['difficulty']:
    for item in most_popular:
        for course in item:
            try:
                for difficulty in user_preferences['difficulty']:
                    if difficulty not in classes_to_difficulty[course]:
                        print(f'Removed {course} from results')
                        most_popular.remove(course)
                        Final_results.append(course)
            except:
                pass
if user_preferences['difficulty']:
    for item in strongly_suggested:
        for course in item:
            try:
                for difficulty in user_preferences['difficulty']:
                    if difficulty not in classes_to_difficulty[course]:
                        print(f'Removed {course} from results')
                        strongly_suggested.remove(course)
                        Final_results.append(course)
            except:
                pass

#map all the reverse maps
df['subject'] = df['subject'].map(reverse_subject_map)
df['career'] = df['career'].map(reverse_career_map)
df['group_pref'] = df['group_pref'].map(reverse_group_map)
df['learning_pref'] = df['learning_pref'].map(reverse_learning_map)

#print(df)
#print("Top 3 Recommended Classes:", top_recommended_classes)
print("Suggested Classes:", Final_results)
print("Strongly Suggested Classes:", strongly_suggested)
print("Most Suggested Classes:", most_popular)
# Visualize the decision tree using matplotlib
plt.figure(figsize=(20,10), dpi=500)
plot_tree(dtree, feature_names=features, class_names=list(elective_map.keys()), filled=True, max_depth=5)
plt.savefig("decision_tree.png", bbox_inches="tight")  # Save to file


