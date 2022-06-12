"""  
    Rock-Paper-Scissors
"""

import random

data = ['R','P','S']
dict_data = {
    'R': 'Rock',
    'P': 'Paper',
    'S': 'Scissors'
}

print('Welcome To Rock-Paper-Scissors')

value = input("pick an option between 'R', 'P' or 'S' >")
going = True
while going :
    if value in data:
        cpu = random.choice(data)
        
        print("Player:("+dict_data[value]+")")
        print("CPU:("+dict_data[cpu]+")")
        if value == cpu:
            value = input("pick an option between 'R', 'P' or 'S' >")
            continue
        elif value == 'R' and cpu == 'P':
            going = False
            print('You lose')
        elif value == 'R' and cpu == 'S':
            going = False
            print('You win')
        elif value == 'P' and cpu == 'R':
            going = False
            print('You win')
        elif value == 'P' and cpu == 'S':
            going = False
            print('You lose')
        elif value == 'S' and cpu == 'R':
            going = False
            print('You lose')
        elif value == 'S' and cpu == 'P': 
            going = False  
            print('You win')
    else:
        value = input("pick an option between 'R', 'P' or 'S' >")
    
    

