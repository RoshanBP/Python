def delete_key_value_pair(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary