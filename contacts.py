import time
print('Hi, stranger!')
# ask for their name
print('What is your name?')
theirName = input()
time.sleep(2)
print('It is good to meet you ' + theirName)
print('The length of your name is: ')
print(len(theirName))
time.sleep(1)
print('What is your age: ')
theirAge = input()
print('Your age will be ' + str(int(theirAge) + 1) + ' in a year.')
time.sleep(2)
print('Bye!')