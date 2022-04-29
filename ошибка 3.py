def is_palindrome(s):
    tmp = s
    tmp = tmp[::-1]
    print(tmp)

    if tmp == s:
        return True
    else:
        return False

def word(n):
    result = []
    for i in range(n):
        element = input('Enter element: ')
        result.append(element)

    if is_palindrome(result):
        print(f"{result} - is palindrom")
    else:
        print(f"{result} - not a palindrom")
word(2)
