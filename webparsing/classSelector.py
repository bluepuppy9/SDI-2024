import json

# Load the data
with open('classes.json', 'r') as f:
    data = json.load(f)

# Example user preferences
user_preferences = {
    'grades': [10, 11],
    'preferred_classes': ['Basketball', 'Fitness'],
    'avoid_classes': ['Dance']
}

def recommend_classes(preferences, data):
    recommended_classes = []

    for category, details in data.items():
        for course in details['courses']:
            course_name, grade_info = course.rsplit(' (', 1)
            grades = grade_info.rstrip(')').split(' - ')
            if any(int(grade) in preferences['grades'] for grade in grades):
                if course_name in preferences['preferred_classes'] and course_name not in preferences['avoid_classes']:
                    recommended_classes.append(course)

    return recommended_classes

recommended_classes = recommend_classes(user_preferences, data)
print("Recommended Classes:")
for cls in recommended_classes:
    print(cls)