import matplotlib.pyplot as plt
import csv
import numpy as np
import math

"""
AIM
To make a graph plotter function that can take input values from csv of Intensities
and then graph them.

"""
class InvalidVoltageError(Exception):

    '''
    Exception raised when the inputed voltage is not
    any of 180V, 200V, 220V
    '''

    def __init__(self, voltage) -> None:
        self.voltage = voltage
        self.message = 'Given voltage "{}V" is invalid. Enter values from 180, 200, 220'.format(voltage)
        super().__init__(self.message)


def data_retriever(voltage:int,slit_width:int, log_graph=False):

    '''
    retrieves data for desired graph from dataset and returns it

    - voltage: from 180V, 200V and 220V, give the int value
    - slit_width: from 1, 2, 3 - referes to the 3 slit widths measured.
    '''

    reader = list(csv.reader(open('dataset.csv', 'r')))
    _reader = list(csv.reader(open('dataset_i_nought.csv')))
    reader.pop(0)
    _reader.pop(0)
    divisor = None
    a_prefix = None

    if voltage == 180:
        a_prefix = 0
        divisor = float(_reader[0][slit_width])
    elif voltage == 200:
        a_prefix = 3
        divisor = float(_reader[1][slit_width])
    elif voltage == 220:
        a_prefix  = 6
        divisor = float(_reader[2][slit_width])
    else:
        raise InvalidVoltageError(voltage)
        
    _target_data = []
    _distances = [float(i[0]) for i in reader]
    if not log_graph:
        for i in reader:
            _target_data.append(float(i[a_prefix + slit_width])/divisor)
        return [[float(x) for x in _distances], [float(x) for x in _target_data]]
    else:
        __distance = []
        for i in reader:
            _target_data.append(math.log(float(i[a_prefix + slit_width])))
        for i in _distances:
            __distance.append(math.log(i))
        return [__distance, _target_data]

    

def plot_curve(_axe, data_points, lined=False, linewidth=1, label=""):
    if not lined:
        _axe.scatter(data_points[0], data_points[1], label=label)
    else:
        _axe.plot(data_points[0], data_points[1], linewidth=linewidth, label=label, marker="o")


fig, ax = plt.subplots(figsize=(8, 6), layout="constrained")
ax.set(ylabel="V/Vₒ", xlabel="Distance (cm)", ylim=(0,1))
ax.grid(True)
slit = 220
data1 = data_retriever(slit, 1)
data2 = data_retriever(slit, 2)
data3 = data_retriever(slit, 3)
ax.set_title(f"{slit}V")
plot_curve(ax, data1, lined=True, linewidth=2, label="1A")
plot_curve(ax, data2, lined=True, linewidth=2, label="2A")
plot_curve(ax, data3, lined=True, linewidth=2, label="3A")
plt.legend()
plt.savefig(f"{slit}.png")