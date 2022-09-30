t=eval(input("enter a tuple:"))
s=input("enter a string:")
t=list(t)
print(t)
l=len(t)
for i in range(0,l*2,2):
    t.insert(i+1,s)
print(t)

    
