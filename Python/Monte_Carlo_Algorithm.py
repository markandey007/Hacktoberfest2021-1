# Estimate the value of pi in range of 0 to 1

import secrets

n = int(input("Enter value of n:"))
no_of_point = 0
total_no_of_point = 0
    
for _ in range(n):
    x = secrets.SystemRandom().uniform(0,1)
    y = secrets.SystemRandom().uniform(0,1)
    distance = x**2 + y**2
    if distance <= 1:
        no_of_point += 1
    total_no_of_point += 1    

pi = 4 * no_of_point/total_no_of_point
print(pi)





