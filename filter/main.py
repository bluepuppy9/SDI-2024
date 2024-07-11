import csv

# Load the data with UTF-8 encoding
with open('classesTech.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

# Example user preferences
user_preferences = {
    'grades': [9],
    'avoid_classes': ['']
}

def recommend_classes(preferences, data):
    recommended_classes = []

    for course in data:
        course_name = course['class']
        course_grades = [int(grade) for grade in course['grades'].split(', ')]
        if any(grade in preferences['grades'] for grade in course_grades):
            if course_name not in preferences['avoid_classes']:
                recommended_classes.append(course_name)
    return recommended_classes

# Call the recommend_classes function
recommended_classes = recommend_classes(user_preferences, data)

# Print the recommended classes
for cls in recommended_classes:
    print(cls)

