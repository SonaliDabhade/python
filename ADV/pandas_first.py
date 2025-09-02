import pandas as pd

student = {
    "id":[101,102,103,104,105],
    "name":["Jhon","Jane","Ron","Harry","Ryan"]
}

df = pd.DataFrame(student)
print(df)
print(pd.__version__)
