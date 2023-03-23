# Exhaustive enumeration

objective = int(input("Choose an integer: "))
answer = 0

while answer**2 < objective:
    answer += 1
    
if answer**2 == objective:
    print(f"The square root of {objective} is {answer}")
else:
    print(f"{objective} does not have an exact square root")