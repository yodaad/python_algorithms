# Approximation algorithm

objective = int(input("Chose a number: "))
epsilon = 0.001
step = epsilon**2
answer = 0.0

while abs(answer**2 - objective) >= epsilon and answer <= objective:
    #print(abs(answer**2 - objective), answer)
    answer += step

if abs(answer**2 - objective) >= epsilon:
    print(f"No square root found for {objective}")
else:
    print(f"The square root of {objective} is {answer}")
    
     


