import csv
import matplotlib.pyplot as plt
import numpy as np

reader = list(csv.reader(open('data.csv', 'r'), quoting=csv.QUOTE_NONNUMERIC))
figure, ax = plt.subplots(1, 1, figsize=(8, 6), layout='constrained')

def get_x_and_y(data:list):
    x = []
    y = []

    for i in data:
        x.append(i[0])
        y.append(i[1])
    x = np.array(x)
    y = np.array(y)
    x = 1/x
    a, b = np.polyfit(x, y, 1)

    return (x, y, a, b)

dat = get_x_and_y(reader)

x = dat[0]
y = dat[1]
ran = np.linspace(0, 1, 100)
ax.scatter(x, y)
ax.plot(ran, dat[2]*ran + dat[3])
plt.show()