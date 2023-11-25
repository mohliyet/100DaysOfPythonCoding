def greet():
    print('Hello!')
    print('How do you do?')
    print('Nice to meet you!')

def greet_with_name(name):
    print(f'Hello {name}')
    print(f'How do you do {name}?')

def greet_with_name_and_location(name,location):
    print(f'Hello {name}.')
    print(f'Are you from {location}?')

greet()
greet_with_name("mohliyet")
greet_with_name_and_location(name='mohliyet',location='AA')
