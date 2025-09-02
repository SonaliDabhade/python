import pandas as pd

Bikes = {
    'names':["Suzuki","Honda"],
    'Average':["14","20"]
}
df = pd.DataFrame(Bikes)
myvar = pd.Series(Bikes)
print(df)
