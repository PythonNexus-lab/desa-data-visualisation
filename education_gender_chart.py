import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the data
df = pd.read_excel("Data_Penduduk_EN.xlsx")

# Optional: check columns
print(df.columns)

# Step 2: Group by 'last education' and 'sex'
grouped = df.groupby(['last education', 'sex']).size().unstack(fill_value=0)

# Step 3: Plot the chart
grouped.plot(kind='bar')
plt.title("Education and Gender Comparison")
plt.xlabel("Education Level")
plt.ylabel("Number of Citizens")
plt.xticks(rotation=45)
plt.legend(title="Gender")
plt.tight_layout()
plt.show()
