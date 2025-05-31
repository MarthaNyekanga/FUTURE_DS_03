# Demographic Data Cleaning and Analysis on Social Media Puchases in the USA

This project involves cleaning and analyzing a demographic dataset using Python and Pandas in Visual Studio Code. The dataset contains fields such as Age, Gender, and Location, and is prepared to support demographic analysis of social media purchasing behavior across selected regions in the USA.

## 📌 Project Objectives

- Clean raw data by handling missing values
- Standardize column naming
- Extract meaningful demographic insights based on age, gender, and location

## 📁 Files and Structure

- `data.csv`  - Kaggle
- `clean_data.py` — Python script used for data cleaning and analysis
- `README.md` — Project documentation

## 🧹 Data Cleaning Steps

- Dropped rows with missing values in important columns such as Age and Gender
- Renamed column headers to have capitalized names for consistency
  df.columns = [col.capitalize() for col in df.columns]

📊 Analysis
Once cleaned, the dataset was used to:

Group and analyze users by age brackets

Understand gender distribution

Identify user concentration by location/state

🛠 Technologies Used
Python 3.x
Pandas
VS Code
Data Source: Kaggle

🚀 How to Run
Clone this repository: https://github.com/MarthaNyekanga/FUTURE_DS_03

Install required packages (if not already installed):

bash
Copy
Edit
pip install pandas

Run the script:

bash
Copy
Edit
python clean_data.py
📬 Contact
For questions, feedback, or collaboration:

Email: [mnyekanga@gmail.com]
