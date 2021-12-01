# HW DRAW THIS: # * * # * * # * * ...
# 9 size

symbol = 1


print("\n")

while symbol <= 9:
    if symbol % 3 == 1:
        print("#",end=" ")
    else:
        print("*",end=" ")
            
    symbol += 1

print("\n")