import pandas as pd

jobs_df = pd.read_csv("Uncleaned_DS_jobs.csv")

if 'index' in jobs_df.columns:
  jobs_df = jobs_df.drop(columns=['index'])

print("\n--- Data före rensning ---")
print(jobs_df.info())
print(jobs_df.head())

def extract_min_salary(salary):
    try:
        if salary == '-1':
            return None
        salary = salary.lower().replace('employer provided salary:', '').replace('(glassdoor est.)', '')
        min_val = salary.split('-')[0].replace('$', '').replace('k', '').strip()
        return int(min_val) * 1000
    except:
        return None

def extract_max_salary(salary):
    try:
        if salary == '-1':
            return None
        salary = salary.lower().replace('employer provided salary:', '').replace('(glassdoor est.)', '')
        max_val = salary.split('-')[1].replace('$', '').replace('k', '').strip()
        return int(max_val) * 1000
    except:
        return None

jobs_df['Min Salary'] = jobs_df['Salary Estimate'].apply(extract_min_salary)
jobs_df['Max Salary'] = jobs_df['Salary Estimate'].apply(extract_max_salary)

jobs_df['Founded'] = jobs_df['Founded'].apply(lambda x: x if x > 0 else pd.NA)

def count_competitors(value):
    try:
        if value == '-1' or pd.isna(value):
            return 0
        return len(value.split(','))
    except:
        return 0

jobs_df['Competitor Count'] = jobs_df['Competitors'].apply(count_competitors)

jobs_df.to_csv("cleaned_DS_jobs.csv", index=False)
print("\n Filen sparad!")