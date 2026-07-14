def z_score(x: float, mean: float, std: float) -> float:
    return (x - mean) / std

result = z_score(10, 5, "2")   # passing a string where a float is expected
