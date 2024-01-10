# we are goint to use some oprtators
# + - * / %
# % - is for getting remainder

#------------------------------------------
# x = int(input("What is x?"))

# if x % 2 == 0:
#     print("even right!")
# else:
#     print("ODD")
    
#------------------------------------------



# another way with function

#------------------------------------------
# def main():
#     x = int(input("What is x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# main()
#------------------------------------------



# More improvement!!!!!

#------------------------------------------
# def main():
#     x = int(input("What is x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     return True if n % 2 == 0 else False
    
# main()
#------------------------------------------


#More!!!!!!!!!!!!!!!!!!!!!!!!

#------------------------------------------
def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return (n % 2 == 0)
    
main()


#------------------------------------------
