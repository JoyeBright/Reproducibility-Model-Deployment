import numpy as np
import pandas as pd
import random

data = np.random.rand(4, 3)
df = pd.DataFrame(data, columns=["A", "B", "C"])
print(df)

print(np.random.randint(0, 100))
