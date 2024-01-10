# i = 3
# while i != 0:
#     print("meow") 
#     i = i-1  
    
     
#     you need to decrement the value 
#     if you decrement it avoids the infinite iterations
    
# you can change the logic

# i = 0
# while i < 3:
#     print("meow")
#     i += 1


# FOR LOOP

# for _ in range(3):
#     print("meow")
    
# Or you can print like this
# print("meow\n" * 3, end = "") #This can print 3 times


while True:
    n = int(input("Give n:"))
    if n < 0:
        continue
    else:
        break
for _ in range(n):
    print("meow")