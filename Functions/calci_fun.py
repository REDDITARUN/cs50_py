def main():
    x = int(input("What is x?"))
    print("x squared is", square(x))
    
def square(n):
    # return n*n   # this is one way
    return n ** 2  # this is n power 2
main()