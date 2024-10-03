n = 5
for i in range(n):#no of rows
    for j in range(i,n-1): #columns that print spaces
        print(" ",end=" ")
    for j in range(i+1): #columns that print '*'
        print("*", end=" ")
    print()


'''    
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''