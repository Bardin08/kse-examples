def is_list(x):
    return isinstance(x, list)


input_data = [1, [7, 8, [9, 10]], 2, [3, 4, [5, 6]]]
res = input_data

while len(list(filter(is_list, res))) > 1:
    for nested_list in res:
        if not isinstance(nested_list, list):
            pass
        else:
            for item in nested_list:
                res.append(item)
            res.remove(nested_list)

print(res)


# -- V2 --

def flat(flatten_list, it):
    if not isinstance(it, list):
        flatten_list.append(it)
        return

    for i in it:
        if not isinstance(i, list):
            flatten_list.append(i)
        else:
            flat(flatten_list, i)


res = []

for i in input_data:
    flat(res, i)

print(res)
