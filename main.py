import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')
df.drop(columns=['Cabin'], inplace=True)
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.savefig('visuals/survival_count.png')
plt.show()

sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Survival by Sex')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.legend(title='Sex (0=Male, 1=Female)')
plt.savefig('visuals/survival_by_sex.png')
plt.show()

sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('visuals/age_distribution.png')
plt.show()

sns.countplot(x='Survived', hue='Pclass', data=df)
plt.title('Survival by Passenger Class')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.legend(title='Pclass')
plt.savefig('visuals/survival_by_pclass.png')
plt.show()

# Insights manually written after observing the above plots
print("\nInsights:")
print("More passengers did not survive (0) than those who did (1).")
print("Females had a much higher survival rate than males.")
print("Most passengers aged between 20 and 40 with a peak around age 28.")
print("1st class passengers had better chances of survival than other class.")
