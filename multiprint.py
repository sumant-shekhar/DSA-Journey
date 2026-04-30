# Given two inputs that are stored in variables a and n, 
# you need to print a, n times in a single line without space between them. 
# Output must have a newline at the end.
a = input()
n = int(input())
#code here
for i in range(1,n+1):
    if n > 0:
        print(a,sep="",end="")
print()