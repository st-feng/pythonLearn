dict1 = {'gallahad': 'the pure', 'robin': 'the brave'}
list1 = ['name', 'quest', 'favorite color']
list2 = ['lancelot', 'the holy grail', 'blue']

for k, v in dict1.items():
    print(f'key:{k}   vulues: {v}')

for i, v in enumerate(list1):
    print(f'index: {i}    value: {v}')

for i, v in zip(list1, list2):
    print(f'What is your {i}?  It is {v}.')

# key:gallahad   vulues: the pure
# key:robin   vulues: the brave
# index: 0    value: name
# index: 1    value: quest
# index: 2    value: favorite color
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.