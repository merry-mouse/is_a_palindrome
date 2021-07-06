def check_if_palindrome():
    string_to_check = str(input("Please enter your word/phrase to ckeck if it's a palindrome : \n"))
    reverse = string_to_check[::-1] # method2
    if string_to_check.lower() == reverse:
        print("Your string {} is a palindrome! ".format(string_to_check))
    else:
        print("Your string {} is not a palindrome! ".format(string_to_check))
check_if_palindrome()