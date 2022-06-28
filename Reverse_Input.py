#Reverse Input

def my_reverse_function(x):
    return x[::-1]




suggestion = 'Y' or 'y'
question = '\nWould you like to see anything else backwards (Y/N) \n'

while suggestion == 'Y' or 'y':

    user_input = input("\nType something to see it wrote backwards? \n")
    user_input = my_reverse_function(user_input)
    
    print(user_input)
    suggestion = input(f"{question}")
