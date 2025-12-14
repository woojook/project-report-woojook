import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.GraphUtils import GraphUtils

df = pd.read_csv("forestfires.csv")

df['log_area'] = np.log(df['area'] + 1)

cols_to_use = ['temp', 'RH', 'wind', 'rain', 'FFMC', 'DMC', 'DC', 'ISI', 'log_area']
data = df[cols_to_use].copy()
data_array = data.to_numpy()

cg = pc(data_array, alpha=0.2)

labels = [f"{col}" for col in data.columns]
pyd = GraphUtils.to_pydot(cg.G, labels=labels)
pyd.write_png('forest_fire_graph2.png')

