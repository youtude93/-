def even(n):
    if n > 3:
        return True
    else:
        return False

a = 3
b = 4
c =-1

assert even(a) == False, "Your code fails!"
assert even(b) == True, "Your code fails!"
assert even(c) == False, "Your code fails!"
print("Success!")
