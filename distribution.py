import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("forestfires.csv")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].hist(df['area'], bins=30, color='red', alpha=0.7)
ax[0].set_title("Raw Distribution of Fire Area")
ax[0].set_xlabel("Area (ha)")
ax[0].set_ylabel("Frequency")

ax[1].hist(np.log(df['area'] + 1), bins=30, color='green', alpha=0.7)
ax[1].set_title("Log-Transformed Distribution")
ax[1].set_xlabel("Log(Area + 1)")

plt.tight_layout()
plt.savefig('data_distribution.png')
print("Saved data_distribution.png")