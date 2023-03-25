# Binary Search Algorithm

objective = int(input("Chose a number: "))
epsilon = 0.0001
low = 0.0
top = max(1.0, objective)
answer = (top + low) / 2

while abs(answer**2 - objective) >= epsilon:
    #print(f"low= {low}, top= {top}, answer= {answer}")
    if answer**2 < objective:
        low = answer
    else:
        top = answer
    answer = (top + low) / 2

print(f"The square root of {objective} is {answer}")

 
