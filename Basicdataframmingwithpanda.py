import pandas as pd
import numpy as np


data ={
    "Name":["Will","zalu","kir","auo","zeo"],
    "Age":[23,42,32,21,44]


}

seri = pd.DataFrame(data ,index = [1,2,3,4,5])

seri["job"] = ["cook","cook","cook","cook","mike"] # new colum
newrow = pd.DataFrame([{"Name":"Sandy","Age":34,"job":"cook"}],index=[6])#new row 
seri = pd.concat([seri,newrow])

print(seri)
