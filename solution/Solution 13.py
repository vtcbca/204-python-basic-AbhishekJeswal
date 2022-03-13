'''WAS to enter any number to print following pattern

 *****
  ****
   ***
    **
     * '''
n=int(input("enter any number:"))
for x in range(n,0,-1):
      for y in range(n,0,-1):
            if x>=y:
                  print(" *",end="")
            else:
                  print("  ",end="")
      print()
      
