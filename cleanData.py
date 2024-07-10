import pandas as pd

# Load data from CSV (replace 'responses.csv' with your file path)
df = pd.read_csv('responses.csv')

# Example cleaning for hobbies field
def clean_hobbies(text):
    # Convert to lowercase, remove extra spaces, and ensure standardized format
    return text.lower().replace(", ", ",")

# Clean hobbies column
df['hobbies'] = df['hobbies'].apply(clean_hobbies)

# Example cleaning for interests or other fields
# Add similar functions for other fields as needed

# Save cleaned data back to CSV (optional)
df.to_csv('cleaned_responses.csv', index=False)

# Now, df contains cleaned and standardized data ready for further processing