def compute_average(values):
    total = 0
    for i in range(len(values)):
        total = total + values[i]
    average = total / len(values)
    return average
