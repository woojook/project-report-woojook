import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.GraphUtils import GraphUtils

url = "forestfires.csv"
df = pd.read_csv(url)

print("Data loaded successfully.")
print(df.head())