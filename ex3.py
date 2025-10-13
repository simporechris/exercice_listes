palindrome = "Un radata na."
ls_palindrome = list(palindrome)
print(ls_palindrome)
print("*"*10)
#1
ls_palindrome[0] = "u"
print(ls_palindrome)
print("*"*10)
#2
ls_palindrome[7] ="r"
print(ls_palindrome)
print("*"*10)
#3
ls_palindrome[11] = "u"
print(ls_palindrome)
print("*"*10)
#4
ls_palindrome.remove(".")
print(ls_palindrome)
print("*"*10)
#5
ls_palindrome.pop(9)
print(ls_palindrome)
print("*"*10)
#6
ls_palindrome.remove("")
print(ls_palindrome)
print("*"*10)

