
import pandas as pd

# Read txt file
df = pd.read_csv("Pasted text (2).txt")

# Save as csv
df.to_csv(
    "epa-sea-level.csv",
    index=False
)

print("CSV created successfully!")
