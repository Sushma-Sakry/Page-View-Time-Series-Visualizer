
import pandas as pd

# Read txt file
df = pd.read_csv("Pasted text (1).txt")

# Save as csv
df.to_csv(
    "fcc-forum-pageviews.csv",
    index=False
)

print("CSV file created successfully!")
