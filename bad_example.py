import numpy as np
import pandas as pd

def compute_average(values):
    total = 0
    for i in range(len(values)):
        total = total + values[i]
    average = total / len(values)
    return average

result = compute_average([1, 2, 3, 4, 5])
print(result)
