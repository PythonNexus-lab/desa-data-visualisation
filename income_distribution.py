import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
df = pd.read_excel("Data_Penduduk_EN.xlsx")

# Step 2: Categorize income
def categorize_income(income):
    if income <= 1_000_000:
        return "Very Low"
    elif income <= 3_000_000:
        return "Low"
    elif income <= 6_000_000:
        return "Middle"
    else:
        return "High"

# Apply the function to create a new column
df['Income Category'] = df['Monthly Income'].apply(categorize_income)

# Step 3: Count how many people are in each category
category_counts = df['Income Category'].value_counts()

# Step 4: Display the pie chart
category_counts.plot.pie(
    autopct='%1.1f%%',
    startangle=90,
    shadow=True,
    colors=['#ff9999','#66b3ff','#99ff99','#ffcc99']
)
plt.title("Income Distribution of Citizens")
plt.ylabel("")  # Hide the y-label
plt.tight_layout()
plt.show()
