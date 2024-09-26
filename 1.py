import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("Housing.csv")
data = list(map(lambda values: [values[0], values[1], values[2], values[4]], data.values))

plt.subplots_adjust(hspace=0.5)

plt.subplot(2, 2, 1)
plt.hist2d(
  x = list(map(lambda value: value[0], data)),
  y = list(map(lambda value: value[1], data))
)
plt.title("Ev fiyatları ev metrekaresi ilişkisi")
plt.xlabel("Ev fiyatı")
plt.ylabel("Ev metrekaresi")

plt.subplot(2, 2, 2)
plt.hist2d(
  x = list(map(lambda value: value[0], data)),
  y = list(map(lambda value: value[2], data))
)
plt.title("Ev fiyatları yatak odası sayısı ilişkisi")
plt.xlabel("Ev fiyatı")
plt.ylabel("Yatak odası sayısı")

plt.subplot(2, 2, 3)
plt.hist2d(
  x = list(map(lambda value: value[0], data)),
  y = list(map(lambda value: value[3], data))
)
plt.title("Ev fiyatları kat sayısı ilişkisi")
plt.xlabel("Ev fiyatı")
plt.ylabel("Kat sayısı")

plt.show()