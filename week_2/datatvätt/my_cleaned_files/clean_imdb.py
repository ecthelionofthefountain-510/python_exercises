import pandas as pd

imdb_df = pd.read_csv("messy_IMDB_dataset.csv", sep=";")

imdb_df = imdb_df.rename(columns={
    'IMBD title ID': 'IMDB_title_ID',
    'Original titl�': 'Original_title',
    'Release year': 'Release_year',
    'Genr�': 'Genre',
    'Content Rating': 'Content_Rating',
    ' Votes ': 'Votes'
})

if 'Unnamed: 8' in imdb_df.columns:
    imdb_df.drop(columns=['Unnamed: 8'], inplace=True)

def clean_income(value):
    try:
        return float(str(value).replace("$", "").replace(",", "").replace(" ", ""))
    except:
        return None
    
imdb_df['Income'] = imdb_df['Income'].apply(clean_income)

def clean_votes(value):
    try:
        return int(str(value).replace(".", "").replace(",", "").replace(" ", ""))
    except:
        return None
    
imdb_df['Votes'] = imdb_df['Votes'].apply(clean_votes)

def clean_score(value):
    try:
        return float(str(value).replace(",", ".").replace(" ", "").replace("+", "").replace(":", "").replace("..", "."))
    except:
        return None
    
imdb_df['Score'] = imdb_df['Score'].apply(clean_score)

def clean_year(value):
    try:
        year = int(str(value)[:4])
        if 1990 <= year <= 2100:
         return year
    except:
         return None
    
imdb_df['Release_year'] = imdb_df['Release_year'].apply(clean_year).astype('Int64')

def clean_duration(value):
    try:
        return int(str(value).replace("Nan", "").replace("Inf", ""))
    except:
        return None
    
imdb_df['Duration'] = imdb_df['Duration'].apply(clean_duration)

print(imdb_df.info())
print(imdb_df.head())

imdb_df.to_csv("cleaned_IMDB_dataset.csv", index=False)
print("\n Filen sparad!")

