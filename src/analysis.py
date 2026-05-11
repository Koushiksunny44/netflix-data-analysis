import pandas as pd
import matplotlib.pyplot as plt

# Load Netflix dataset
df = pd.read_csv("data/netflix_titles.csv")

# Display dataset
print("\n=== Netflix Dataset ===")
print(df.head())

# Count Movies vs TV Shows
content_counts = df["type"].value_counts()

print("\n=== Movies vs TV Shows ===")
print(content_counts)

# Plot content type distribution
content_counts.plot(kind="bar")

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")

plt.tight_layout()

# Save chart
plt.savefig("images/content_type_chart.png")

# Show chart
plt.show()

# Analyze top genres
genres = df["listed_in"].str.split(", ").explode()

top_genres = genres.value_counts().head(10)

print("\n=== Top 10 Genres ===")
print(top_genres)

# Plot top genres
top_genres.plot(kind="bar")

plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Count")

plt.tight_layout()

# Save chart
plt.savefig("images/top_genres_chart.png")

# Show chart
plt.show()