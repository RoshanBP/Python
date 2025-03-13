my_dict = {}

def add_element(key, value):
    my_dict[key] = value

def update_element(key, value):
    my_dict[key] = value

add_element("name", "John")
add_element("age", 30)
print(my_dict)  

update_element("age", 35)
print(my_dict)  