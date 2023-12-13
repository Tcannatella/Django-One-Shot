def reverse_entries(dictionary):
    result = {}
    for key, value in dictionary.items():
        result[value] = key
    return result

new = {'hair': 'red', 'eyes': 'blue'}
print(reverse_entries(new))
