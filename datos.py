import pandas as pd
df = pd.DataFrame({'x': [0, 1], 'y': [0, 1], 'z': [0, 1], 'pressure': [100, 150]})
df.to_csv('output.csv', index=False)