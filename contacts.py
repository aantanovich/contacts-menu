supplies = ['pens', 'cans', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

supplies += ['penciles']
print(supplies[:])
supplies.insert(2, 'fans')
print(supplies[:])
del supplies[-1]
print(supplies[:])