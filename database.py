from web_parse import person_quotes
import pandas as pd



df = pd.DataFrame.from_dict(person_quotes, orient="index")

print(df)