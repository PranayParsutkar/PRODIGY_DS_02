# PRODIGY_DS_02
This project involves data cleaning and exploratory data analysis (EDA) on the Titanic dataset from Kaggle. The dataset is cleaned by handling missing values and converting categorical features into numerical form. Key visualizations are created to explore survival patterns based on gender, passenger class, and age. The project helps uncover important insights about the factors that influenced passenger survival during the Titanic disaster.

## Dataset Used
- Filename: train.csv  
- Source: [Kaggle Titanic Challenge](https://www.kaggle.com/c/titanic/data)

## Tools and Libraries Used
- Python
- pandas
- seaborn
- matplotlib

## How to Run the Project
1. Clone this repository or download the files.
2. Make sure you have Python installed with the following libraries:
   `bash
   pip install pandas seaborn matplotlib
3. Run the Python script:
   python main.py
4. The plots will be saved inside the visuals folder.

## Exploratory Data Analysis (EDA)
To understand survival patterns, I generated 4 visual plots using seaborn and matplotlib:
1. Survival Count  
   Shows the overall number of passengers who survived vs. who didn't.
2. Survival by Sex  
   Displays how gender affected survival rates.
3. Age Distribution  
   Visualizes the age range of passengers on board.
4. Survival by Passenger Class  
   Analyzes how socio-economic class (Pclass) influenced survival chances.

## Output Plots
All plots are saved in a folder named visuals automatically when the code is executed.
Saved plot files: 
1. survival_count.png
2. survival_by_sex.png
3. age_distribution.png
4. survival_by_pclass.png

## Insights (From Visual Plots)
1. More passengers did not survive (label 0) than those who did (label 1), showing an overall survival rate of less than 50%.
2. Females had a significantly higher survival rate than males — most female passengers survived.
3. The age distribution was centered around 20–40 years, with many passengers aged around 28.
4. 1st class passengers had the highest survival rate, while 3rd class had the lowest, showing class inequality in survival chances.