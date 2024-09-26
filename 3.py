import pandas
import matplotlib.pyplot as plt
import seaborn as sns

data = pandas.read_csv("Housing.csv")

sns.heatmap(data.select_dtypes(["number"]).corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Korelasyon Matrisi")
plt.show()
