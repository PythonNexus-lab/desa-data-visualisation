import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Excel file
df = pd.read_excel("Data_Penduduk_EN.xlsx")

# Step 2: Display column names (to double-check structure)
print("Available Columns:", df.columns)

# Step 3: Group and count by 'Profesi'
occupation_counts = df['Profesi'].value_counts()

# Step 4: Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(occupation_counts, labels=occupation_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Percentage of Occupations in Desa Cibodas")
plt.axis('equal')  # makes the pie chart a circle
plt.show()
