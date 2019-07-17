def palindrome(s):
    return s == s[::-1]
    
if _name_ == '_main_':
    s = input('Enter a string: ')
    if palindrome(s):
        print('Yay a palindrome')
    else:
        print('Oh nom not a palindrome')