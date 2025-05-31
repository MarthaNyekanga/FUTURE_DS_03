import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('customer_dataset.csv')  


print(df.head())

# Check column names
print(df.columns)

# Capitalize the first letter of each column name
df.columns = [col.capitalize() for col in df.columns]

# Drop rows with missing values in critical columns
df = df.dropna(subset=['Age', 'Gender', 'Location'])

# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Convert age to numeric
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Age distribution summary
print(df['age'].describe())

# Group age into categories
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 25, 35, 50, 100],
                         labels=['<18', '18-25', '26-35', '36-50', '50+'])

# Age group count
print(df['age_group'].value_counts())

# Gender count
print(df['gender'].value_counts())

# Gender count
print(df['gender'].value_counts())

# State distribution
print(df['location'].value_counts().head(10))



# Age group plot
sns.countplot(data=df, x='age_group')
plt.title('Age Group Distribution')
plt.show()

# Gender plot
sns.countplot(data=df, x='gender')
plt.title('Gender Distribution')
plt.show()
