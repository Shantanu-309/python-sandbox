
import numpy as np

import pandas as pd

df = pd.read_csv("#Yourpokemon csv file ",index_col="Name")
while True:

  pokename = input("enter a pokemon name ")
  try:
     print(df.loc[pokename])
  except KeyError:
     print(f"{pokename} does not exist maybey you misspelled try again ")
