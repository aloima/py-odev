import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("Housing.csv")
data = list(map(lambda values: [values[0], values[3], values[12]], data.values))
result = []

for house in data:
  if list(map(lambda value: value[1], result)).__contains__(house[1]):
    val = result[list(map(lambda value: value[1], result)).index(house[1])]
    val[0] += house[0]
    val[2] += 1
  else:
    result.append([house[0], house[1], 1])

for value in result:
  value[0] /= value[2]
  value.pop(2)

plt.subplot(1, 2, 1)

plt.bar(list(map(lambda value: value[1], result)), list(map(lambda value: value[0], result)))
plt.title("Ev fiyatlarının banyo sayısına göre dağılımı")
plt.xlabel("Banyo sayısı")
plt.ylabel("Ev fiyatı")

result = []

for house in data:
  if list(map(lambda value: value[1], result)).__contains__(house[2]):
    val = result[list(map(lambda value: value[1], result)).index(house[2])]
    val[0] += house[0]
    val[2] += 1
  else:
    result.append([house[0], house[2], 1])

for value in result:
  value[0] /= value[2]
  value.pop(2)

plt.subplot(1, 2, 2)

plt.bar(list(map(lambda value: value[1], result)), list(map(lambda value: value[0], result)))
plt.title("Ev fiyatlarının mobilya durumuna göre dağılımı")
plt.xlabel("Mobilya durumu")
plt.ylabel("Ev fiyatı")

plt.show()