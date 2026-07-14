def z_score(x, mean, std):
    if std == 0:
        raise ValueError("standard deviation cannot be zero")
    return (x - mean) / std
