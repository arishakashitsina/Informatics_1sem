s = input()

pairs = [('E', '3'), ('3', 'E'), ('J', 'L'), ('L', 'J'), ('S', '2'), ('2', 'S'), ('Z', '5'), ('5', 'Z'), ('A', 'A'),
         ('H', 'H'), ('I', 'I'), ('M', 'M'), ('O', 'O'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'),
         ('Y', 'Y'), ('1', '1'), ('8', '8')]
a = dict(pairs)

def check_is_mirror(s):
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] not in a:
            return 0
        if s[j] not in a:
            return 0
        if a[s[i]] != s[j]:
            return 0
        i += 1
        j -= 1
    return 1

def check_is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return 0
        i += 1
        j -= 1
    return 1

fl1 = check_is_mirror(s)
fl2 = check_is_palindrome(s)

if fl1 == 1 and fl2 == 1:
    print(s, "is a mirrored palindrome.")
elif fl1 == 1:
    print(s, "is a mirrored string.")
elif fl2 == 1:
    print(s, "is a regular palindrome.")
else:
    print(s, "is not a palindrome.")