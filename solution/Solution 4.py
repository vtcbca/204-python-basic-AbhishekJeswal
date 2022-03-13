#WAS enter 3 number and print which number maximum number
n1,n2,n3=[int(n) for n in input("enter three values:").split()]
if n1>n2 and n1>no3:
    l=n1
elif n2>n1 and n2>n3:
    l=n2
else:
    l=n3
print("{} is the maximum number".format(l))
