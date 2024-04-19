#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    lower_case = word.lower()
    remove_space = lower_case.replace(" ", "")
    first_half = remove_space[:len(remove_space)//2]
    second_half = remove_space[len(remove_space)//2]
    if remove_space == "":
        return False
    elif first_half[0] == second_half[-1]:
       return True
    else:
        return False 

if __name__ == '__main__': 
    user_input = input()
    print(palindrome(user_input))

