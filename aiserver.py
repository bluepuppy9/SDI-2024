#from flask import Flask, request, jsonify
#from flask_cors import CORS
#from time import sleep
#
#from ollama import generate
#
#app = Flask(__name__)
#CORS(app)
#
#
#@app.route('/chat', methods=['POST'])
#def chat():
#    user_input = request.json.get('message').lower()
#    message = ''
#    for part in generate('llama3', user_input, stream=True):
#        message += part['response']
#    #return jsonify({'response': "the mitocondira is actually the powerhouse of the cell"})
#    #return jsonify({'response': f"{user_input} for real"})
#    return jsonify({'response': message})
#if __name__ == '__main__':
#    app.run(debug=True)
import re
from typing import List, Dict

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
        'easy': ['easy', 'not hard', 'simple'],
        'medium': ['medium', 'moderate', 'not that hard'],
        'hard': ['hard', 'difficult', 'challenging'],
    }
    for level, keywords in difficulty_keywords.items():
        for keyword in keywords:
            if re.search(rf'\b{re.escape(keyword)}\b', text, re.IGNORECASE):
                return level
    return "unknown"

def check_grade(text: str) -> str:
    grade_pattern = re.compile(r'\b(9th|10th|11th|12th|freshman|sophomore|junior|senior|freshmen|sophomores|juniors|seniors)\b', re.IGNORECASE)
    match = grade_pattern.search(text)
    return match.group(0).lower() if match else "unknown"

def check_career_path(text: str) -> List[str]:
    career_keywords = {
        'Law': ['law', 'lawyer', 'attorney', 'legal'],
        'Finance': ['finance', 'financial', 'banking', 'accounting', 'economics'],
        'Medicine': ['medicine', 'doctor', 'physician', 'medical', 'healthcare'],
        'Software Development': ['software development', 'software', 'programmer', 'developer', 'coding'],
        'Teaching/Education': ['teaching', 'teacher', 'education', 'educator', 'professor'],
        'Marketing': ['marketing', 'advertising', 'brand', 'promotion'],
        'Data Science': ['data science', 'data scientist', 'data', 'analytics'],
        'Psychology': ['psychology', 'psychologist', 'therapist', 'counseling'],
        'Environmental Science': ['environmental science', 'environment', 'ecology', 'conservation'],
        'Music Production': ['music production', 'music', 'producer', 'audio'],
        'Culinary Arts': ['culinary arts', 'chef', 'cooking', 'cuisine'],
        'Engineering': ['engineering', 'engineer'],
        'Graphic Design': ['graphic design', 'design', 'graphic designer'],
        'Movie/Show Production': ['movie production', 'show production', 'film', 'cinema', 'television'],
        'Entrepreneur': ['entrepreneur', 'business', 'startup', 'enterprise'],
        'Architecture': ['architecture', 'architect', 'building design']
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
    group_keywords = ['group', 'team', 'collaborate', 'together']
    not_group_keywords = ['alone', 'individual', 'single']
    for keyword in group_keywords:
        if re.search(rf'\b{re.escape(keyword)}\b', text, re.IGNORECASE):
            return "yes"
    for keyword in not_group_keywords:
        if re.search(rf'\b{re.escape(keyword)}\b', text, re.IGNORECASE):
            return "no"
    return "unknown"

# Example subjects list with keywords and abbreviations

# Example input text
classes = [
{'name': 'AP English (Language or Literature) & Composition', 'keywords': ['AP English', 'AP English Language', 'AP English Literature', 'AP Lang', 'AP Lit']},
{'name': 'AP Calculus (AB or BC)', 'keywords': ['AP Calculus', 'AP Calc AB', 'AP Calc BC']},
{'name': 'AP Statistics', 'keywords': ['AP Statistics', 'AP Stats']},
{'name': 'AP Biology', 'keywords': ['AP Biology', 'AP Bio']},
{'name': 'AP Chemistry', 'keywords': ['AP Chemistry', 'AP Chem']},
{'name': 'AP Physics (1, 2 or C)', 'keywords': ['AP Physics', 'AP Physics 1', 'AP Physics 2', 'AP Physics C']},
{'name': 'AP Environmental Science', 'keywords': ['AP Environmental Science', 'AP Enviro Sci']},
{'name': 'AP Psychology', 'keywords': ['AP Psychology', 'AP Psych']},
{'name': 'AP US Government & Politics', 'keywords': ['AP US Government', 'AP US Gov', 'AP Gov & Pol']},
{'name': 'AP Macroeconomics', 'keywords': ['AP Macroeconomics', 'AP Macro']},
{'name': 'AP Computer Science Principles', 'keywords': ['AP Computer Science Principles', 'AP Comp Sci', 'AP Comp Sci Principles']},
{'name': 'Adv. C.A.D. Civil Engineering & Architecture', 'keywords': ['Advanced CAD', 'Advanced CAD Civil Engineering', 'Advanced CAD Architecture']},
{'name': 'Advanced Computer Applications & Development', 'keywords': ['Advanced Computer Applications', 'Advanced Computer Development']},
{'name': 'Adv. AV Engineering & TV Studio (1 through 3)', 'keywords': ['Advanced AV Engineering', 'Advanced TV Studio', 'av', 'into to av']},
{'name': 'Advanced Russian', 'keywords': ['Advanced Russian']},
{'name': 'Applied Physics', 'keywords': ['Applied Physics']},
{'name': 'Behavioral & Social Science Class', 'keywords': ['Behavioral Science', 'Social Science']},
{'name': 'Biotechnology', 'keywords': ['Biotechnology', 'BioTech']},
{'name': 'Creative Writing', 'keywords': ['Creative Writing']},
{'name': 'Computer Science & Engineering', 'keywords': ['Computer Science', 'Computer Engineering', 'Comp Sci']},
{'name': 'C.A.D / Civil Engineering & Architecture', 'keywords': ['CAD Civil Engineering', 'CAD Architecture']},
{'name': 'Career Financial Management & Entrepreneurship', 'keywords': ['Career Financial Management', 'Entrepreneurship']},
{'name': 'College Russian', 'keywords': ['College Russian']},
{'name': 'Concert Bands', 'keywords': ['Concert Bands']},
{'name': 'Chamber Music', 'keywords': ['Chamber Music']},
{'name': 'Design & Fabrication (Makerspace)', 'keywords': ['Design and Fabrication', 'Makerspace']},
{'name': 'Electronics & Green Technology', 'keywords': ['Electronics and Green Technology']},
{'name': 'Forensic Science', 'keywords': ['Forensic Science', 'Forensics']},
{'name': 'Fundamentals of Engineering', 'keywords': ['Fundamentals of Engineering']},
{'name': 'Freshmen Band', 'keywords': ['Freshmen Band']},
{'name': 'Human Anatomy & Physiology', 'keywords': ['Human Anatomy', 'Physiology']},
{'name': 'Intro to AV Engineering & TV Studio', 'keywords': ['Intro to AV Engineering', 'Intro to TV Studio']},
{'name': 'Jazz Ensemble', 'keywords': ['Jazz Ensemble']},
{'name': 'Modern Mythology: Gods & Monsters', 'keywords': ['Modern Mythology', 'Gods and Monsters']},
{'name': 'Multivariable Calculus', 'keywords': ['Multivariable Calculus']},
{'name': 'Marching Band', 'keywords': ['Marching Band']},
{'name': 'Publications', 'keywords': ['Publications']},
{'name': 'Public Speaking', 'keywords': ['Public Speaking']},
{'name': 'Russian for Business', 'keywords': ['Russian for Business']},
{'name': 'String Ensemble', 'keywords': ['String Ensemble']},
{'name': 'Symphonic Band', 'keywords': ['Symphonic Band']},
{'name': 'Theater Production', 'keywords': ['Theater Production']},
{'name': 'Wind Ensemble', 'keywords': ['Wind Ensemble', 'Band']},
{'name': 'Work Based Learning (1 or 2)', 'keywords': ['Work Based Learning']}
]

subjects = [
{'name': 'Science', 'keywords': ['science', 'biology', 'chemistry', 'physics', 'environmental science', 'forensic science', 'biotech', 'anatomy']},
{'name': 'Math', 'keywords': ['math', 'mathematics', 'calculus', 'algebra', 'statistics', 'geometry', 'multivariable calculus']},
{'name': 'Ela', 'keywords': ['english', 'ela', 'literature', 'composition', 'creative writing', 'public speaking', 'publications', 'mythology']},
{'name': 'Photography/Videography', 'keywords': ['photography', 'videography', 'film', 'tv studio']},
{'name': 'Robotics', 'keywords': ['robotics']},
{'name': 'History', 'keywords': ['history', 'us government', 'politics', 'macroeconomics']},
{'name': 'Art', 'keywords': ['art', 'drawing', 'painting', 'sculpture', 'fashion', 'design']},
{'name': 'Music', 'keywords': ['music', 'band', 'orchestra', 'ensemble', 'jazz', 'marching band', 'wind ensemble']},
{'name': 'Performing Arts', 'keywords': ['theater', 'theater production', 'dance', 'performing arts']},
{'name': 'Audio Visual (AV)', 'keywords': ['audio visual', 'av', 'video', 'film', 'tv studio', 'audio engineering', 'video engineering']}
]

text = input("Input: ")
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
        found_subjects = check_class_subject(text, subjects)
        classes_found = check_class(text, classes)
    while difficulty_level == 'unknown':
        print(f"Please provide more information about your difficulty level.")
        text = input("Input: ")
        difficulty_level = check_difficulty(text)
    while grade_level == 'unknown':
        print(f"Please provide more information about your grade level.")
        text = input("Input: ")
        grade_level = check_grade(text)
    while career_path == 'unknown':
        print(f"Please provide more information about your career path.")
        text = input("Input: ")
        career_path = check_career_path(text)
    while group_work_preference == 'unknown':
        print(f"Please provide more information about your group work preference.")
        text = input("Input: ")
        group_work_preference = check_group_work(text)
    while classes_found == 'unknown':
        print(f"Please provide more information about any classes you like.")
        text = input("Input: ")
        classes_found = check_class(text, classes)
# Print the results
print("Found Subjects:", found_subjects)
print("Difficulty Level:", difficulty_level)
print("Grade Level:", grade_level)
print("Career Path:", career_path)
print("Group Work Preference:", group_work_preference)
print("Classes Found:", classes_found)


