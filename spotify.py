import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Replace your file.csv with the path to your CSV file
csv_file_path = "/Users/javeriajalil/PycharmProjects/pythonProject/project/spotify.csv"
# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')


# Function to extract numeric values from strings
def extract_numeric(s):
    numeric = ''.join(filter(str.isdigit, str(s)))  # Extract only digits from the string
    return int(numeric) if numeric else None  # Convert the extracted digits to int


# Clean 'streams' column
df['streams'] = df['streams'].apply(lambda x: extract_numeric(x))
# Filter out rows where 'streams' couldn't be converted to int
df = df.dropna(subset=['streams'])

# Top 10 streamed songs data
track_names = [
    "Love Grows (Where My Rosemary Goes)",
    "Blinding Lights",
    "Shape of You",
    "Someone You Loved",
    "Dance Monkey",
    "Sunflower - Spider-Man: Into the Spider-Verse",
    "One Dance",
    "STAY (with Justin Bieber)",
    "Believer",
    "Closer"
]

danceability_values = [
    53, 50, 83, 50, 82, 76, 77, 59, 77, 75
]

stream_values = [
    "1.10 Trillion", "3.703 Billion", "3.562 Billion", "2.887 Billion", "2.864 Billion",
    "2.808 Billion", "2.714 Billion", "2.665 Billion", "2.594 Billion", "2.591 Billion"
]

liveness_values = [17, 9, 9, 11, 18, 7, 36, 10, 23, 11]


def add_labels():
    for i, (name, danceability, stream) in enumerate(zip(track_names, danceability_values, stream_values)):
        plt.text(danceability + 1, i, f'{danceability}% ({stream})', va='center', fontsize=8, ha='left')


# Bar plot for danceability percentage and stream values of top 10 streamed songs
plt.figure(figsize=(12, 10))
bars = plt.barh(track_names, danceability_values, color='skyblue')
add_labels()

plt.xlabel('Danceability (%) and Stream Values')
plt.ylabel('Track Names')
plt.title('Danceability Percentage and Stream Values of Top 10 Streamed Songs')

plt.gca().invert_yaxis()
plt.yticks(rotation=45)
plt.tight_layout()
plt.show()

# Stream Value vs Dancibility scatter plot
plt.figure(figsize=(10, 8))
plt.scatter(danceability_values, stream_values, color='skyblue', s=100)

for i, txt in enumerate(track_names):
    plt.annotate(txt, (danceability_values[i], stream_values[i]), textcoords="offset points", xytext=(5, 5),
                 ha='center')

plt.xlabel('Danceability(%)')
plt.ylabel('Stream Values')
plt.title('Stream Values vs. Danceability')
plt.grid(True)
plt.tight_layout()
plt.show()

# Graph with Dancibility and Liveliness Comparision within top 10 streamed songs
plt.figure(figsize=(12, 10))
bar_width = 0.25
index = np.arange(len(track_names))
bars1 = plt.barh(index - bar_width, danceability_values, bar_width, color='skyblue', label='Danceability')
bars2 = plt.barh(index, liveness_values, bar_width, color='orange', label='Liveness')

# Adding labels to bars (Stream Values)
for i, (d, l, s) in enumerate(zip(danceability_values, liveness_values, stream_values)):
    plt.text(d + 1, i - bar_width, f'{d}%', va='center', fontsize=8, ha='left')
    plt.text(l + 1, i, str(l), va='center', fontsize=8, ha='left')
    plt.text(-1.5, i - bar_width, s, va='center', ha='center', fontsize=8,
             color='black')  # stream values under track names

plt.xlabel('Percentage / Values')
plt.ylabel('Track Names')
plt.title('Comparison of Danceability, Liveness, and Stream Values')

plt.yticks(index, track_names, rotation=0)

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
