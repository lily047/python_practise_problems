print(hash((1,2)))
#prints a random value for objects, like a fingerprint 

arr = map(int, input().split())
#converts each str into an int 

name, *line = input().split()
#*variable collects all remaining items after the variables on the left have taken their share.

print(f"{average_marks:.2f}")
#to force the ouput to be 2 decimal places, by round(x,2) u get a float and by the above method u get a string 
