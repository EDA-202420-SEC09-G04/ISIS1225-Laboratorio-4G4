from . import list_node as Node


def new_list():
    newlist = {"size" : 0,
               "first":None,
               "last":None
               }
    return newlist



def add_first(my_list, element):
    new_node = Node.new_single_node(element)
    new_node["next"] = my_list["first"]
    my_list["first"] = new_node
    if my_list["size"] == 0:
        my_list["last"] = my_list["first"]
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    new_node = Node.new_single_node(element)
    
    if my_list["size"] == 0:
        my_list["first"] = new_node
    else:
        my_list["last"]["next"] = new_node
    my_list["last"] = new_node
    my_list["size"] += 1
    return my_list
    
def is_empty(newlist):
    if newlist['size'] == 0:
        is_empty = True
    else:
        is_empty = False
    return is_empty

def size(my_list):
    return my_list["size"]


def first_element(my_list):
    if my_list["size"] == 0:
        return None
    else: 
        return my_list["first"]["info"]

def last_element(my_list):
    if my_list["size"] == 0:
        return None
    else: 
        return my_list["last"]["info"]

def get_element(my_list, pos):
    first = my_list["first"]
    i = 0
    if my_list["size"] == 0:
        return first["info"]
    else:
        while i < pos:
            first = first["next"]
            i += 1
        return first["info"]
  
def remove_first(my_list):
    if my_list["size"] > 1:
        node = my_list["first"]
        my_list["first"] = my_list["first"]["next"]
        node["next"] = None
        node["element"] = None
        my_list["size"] -= 1
    elif my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] -= 1
    elif my_list["size"] == 0:
        return None
    
    return my_list

def remove_last(my_list):
    
    if my_list["size"] > 1:
        node = my_list["last"]
        ultimo = my_list["first"]
        penultimo = my_list["first"]
        for i in range(my_list['size']-1):
            penultimo = ultimo
            penultimo = ultimo['next']
        my_list["last"] = penultimo
        node["next"] = None
        node["element"] = None
        my_list["size"] -= 1
    elif my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] -= 1
    elif my_list["size"] == 0:
        return None
    return my_list

def insert_element(my_list, element, pos):
    new_node = Node.new_single_node(element)
    if pos == 0:
        add_first(my_list, element)
    elif pos == my_list["size"]:
        add_last(my_list, element)
    else:
        first = my_list['first']
        for i in range(pos):
            antes = first
            first = first['next']
        antes['next'] = new_node
        new_node['next'] = first
        my_list['size'] += 1
    
    return my_list

def is_present(my_list, element, cmp_function):
    if my_list["size"] == 0:
        return -1
    node = my_list["first"]
    i = 0
    while i < my_list["size"]:
        if node is None:
            return -1
        if cmp_function(element, node["info"]) == 0:
            return i
        node = node["next"]
        i += 1
    return -1

def delete_element(my_list, pos):

    if pos == 0:
        my_list['first'] = my_list['first']['next']
        if my_list['size'] == 1:
            my_list['last'] = None
    else:
        node = my_list['first']
        for i in range(pos - 1):
            node = node['next']
        node['next'] = node['next']['next']
        if pos == my_list['size'] - 1:
            my_list['last'] = node

    my_list['size'] -= 1
    return my_list

def change_info(my_list, pos, new_info):
    
    first = my_list["first"]
    i = 0
    while i < pos:
        first = first["next"]
        i += 1
    first["info"] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 == pos2:
        return my_list
    n1 = my_list["first"]
    n2 = my_list["first"]
    i = 0
    while i < pos1:
        n1 = n1["next"]
        i += 1
    i = 0
    while i < pos2:
        n2 = n2["next"]
        i += 1
    info = n1["info"]
    n1["info"] = n2["info"]
    n2["info"] = info
    return my_list

def sub_list(my_list, pos, num, elem):