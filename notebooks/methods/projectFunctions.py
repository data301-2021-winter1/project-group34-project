#Importing libraries 
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (pd.read_csv(url_or_path_to_csv_file).dropna()
             .reset_index(drop=True)
          
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (df1.rename(columns={"listed_in": "Genre", "release_year": "Release Year", "type": "Type"})
              .rename(columns={"title": "Title", "director": "Director", "cast": "Cast"})
              .rename(columns={"show_id": "Show ID", "country": "Country", "date_added": "Date Added"})
              .rename(columns={"rating": "Rating", "duration": "Duration", "description": "Description"})
              .drop(["Description"], axis = 1)
              .sort_values(by = "Show ID", ascending = True)
            
      )

    # Make sure to return the latest dataframe

    return df2 