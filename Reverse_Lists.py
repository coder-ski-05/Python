#Reverse_Lists

def my_reverse_function(x):
    return x[::-1]

camping_gear = ['tent', 'tent poles', 'panco', 'tent cover']


suggestion = 'Y' or 'y'
question = '\nWould you like to see your camping lists again? (Y/N) \n'

while suggestion == 'Y' or 'y':

    user_input = input("\nWould you like details on your camping gear? \n")
    camping_gear = my_reverse_function(camping_gear)



    print(camping_gear)
    print()
    print('You have ', len(camping_gear), ' camping gear items packed!')



    question = input(f"{question}")

