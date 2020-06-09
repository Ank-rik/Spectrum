my_dict = {'physics':88, 'maths':75, 'chemistry':72, 'Basic electrical':89 }

key_max = max(list(my_dict.keys()), key=(lambda k: my_dict[k]))
key_min = min(list(my_dict.keys()), key=(lambda k: my_dict[k]))

print(('Maximum Value: ',my_dict[key_max]))
print(('Minimum Value: ',my_dict[key_min]))
