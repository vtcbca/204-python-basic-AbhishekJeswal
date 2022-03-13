#WAS to enter any number and print the sum of its digit
n=int(input("Enter any value : ")) 
sum=0
while n>0:
    t=n%10
    sum=sum+t
    n=n//10
print("The sum of all degit is {}".format(sum))
