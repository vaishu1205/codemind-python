x=int(input())
temp=x
k=0
for i in range(1,x):
    if(x%i==0):
        k=k+i
if(k>temp):
    print("True")
else:
    print("False")