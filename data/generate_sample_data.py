import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': [f'User{i}' for i in range(10000)],
    'email': [f'user{i}@example.com' for i in range(10000)],
    'score': np.random.randint(1, 100, 10000)
})
df.to_csv('data/sample.csv', index=False)