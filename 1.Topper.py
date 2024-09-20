 #1.To find the Topper of subject wise name
import pandas as pd

def subject_toppers(df):
    toppers = {}
    for subject in df.columns[1:]:
        topper = df.loc[df[subject].idxmax(), 'Student']
        toppers[subject] = topper
    result_df = pd.DataFrame(list(toppers.items()), columns=['Subject', 'Topper'])
    
    return result_df

data = {
    'Student': ['Akhil', 'Bhanu', 'Sintu', 'Rakesh','Manish','Bikash'],
    'Maths': [70, 85, 65, 90, 95, 98],
    'Science': [85, 78, 92, 88, 76, 66],
    'Social': [80, 76, 89, 95, 55, 78],
    'English': [99, 45, 76, 56, 89, 81]
}

df = pd.DataFrame(data)
topper_df = subject_toppers(df)
print(topper_df)


#2. To fill in the missing grades with the average grade of that Subject.

