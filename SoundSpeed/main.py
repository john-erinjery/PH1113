import csv
import matplotlib.pyplot as plt
import numpy as np
reader = list(csv.reader(open('data.csv', 'r'), quoting=csv.QUOTE_NONNUMERIC))
figure, ax = plt.subplots(1, 1, figsize=(8, 6), layout='constrained')

def wavelen_calc(data:list):
    '''
    data should be distances of nodes and antinodes
    [n1, a1, n2, a2] n = node; a = anti-node

    we will take all possible values for wavelenght, avergae them out
    and find wavelength, along with st.dev
    '''
    f, n1, a1, n2, a2 = data
    lambda_values = [(a1-n1)*4, (n2 - a1)*4, (a2 - n2)*4, (n2-n1)*2, (a2 - a1)*2]
    mean = np.mean(lambda_values)
    std = round(np.std(lambda_values), 3)
    
    return f, mean, std



y_values = []
x_values_ = []
err=[]

for i in reader:

    values = wavelen_calc(i)
    y_values.append(values[0])
    x_values_.append(values[1])
    err.append(values[2])
y_values = np.array(y_values)
y_values = y_values/100
ar = np.array(x_values_)
x_values = 1/ar
x_values *= 1000
a, b = np.polyfit(x_values, y_values, 1)
err = np.array(err)
err /= 100
plt.errorbar(x_values, y_values, xerr=err, fmt='o', capsize=1, color='orange', label="Error bars")
plt.scatter(x_values, y_values, s=10, color='skyblue')
x = np.linspace(0, 10, 20)
plt.plot(x, a * x + b, '--', color="skyblue", label=f"slope : {round(a, 4)}")
plt.ylabel('$10^{2}$ Hz')
plt.xlabel('$m^{-1}$')
plt.title('$f$  vs  $1/{\\lambda}$')
plt.legend(loc="upper left")
plt.show()
    