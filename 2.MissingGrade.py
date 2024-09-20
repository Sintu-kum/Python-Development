#2. To fill in the missing grades with the average grade of that Subject.
import pandas as pd

def fill_missing_grades(df):
    for subject in df.columns[1:]:
        subject_mean = df[subject].mean()
        df[subject].fillna(subject_mean, inplace=True)
    
    return df

data = {
    'Student': ['Akhil', 'Bhanu', 'Clara', 'Sintu', 'Makhio'],
    'Math': [85, 70, None, 90, 78],
    'Science': [None, 88, 90, None, 85],
    'English': [78, None, 85, 92, 88],
    'History': [90, 75, None, 88, None]
}

df = pd.DataFrame(data)
filled_df = fill_missing_grades(df)
print(filled_df)


