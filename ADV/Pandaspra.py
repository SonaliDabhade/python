import pandas as pd

Teachers = {
    "id":[101,102,103,104,105],
    "name":["Jhon","Jane","Ron","Harry","Ryan"],
    "Wages":["16K","25k","24k","34k","40k"]
}
df = pd.DataFrame(Teachers)
print(df)