def convert(data):
    if isinstance(data, tuple):
        return list(data)
    elif isinstance(data, list):
        return tuple(data)
    else:
        raise TypeError("Input must be a tuple or a list")