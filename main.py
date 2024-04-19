#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    lower_case = word.lower()
    remove_space = lower_case.replace(" ", "")
    if remove_space[0] == remove_space[-1]:
       return True
    elif remove_space == " ":
        return False
    else:
        return False 

if __name__ == '__main__': 
    user_input = input()
    print(palindrome(user_input))

