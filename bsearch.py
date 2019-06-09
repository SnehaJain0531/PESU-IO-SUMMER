#Code for Question 3
def binarysearch(ar,b,l,num): 
      while b <= l:   
        mid = (l+b)//2;  
        # Check if x is present at mid 
        if ar[mid] == num: 
            return mid 
        elif ar[mid] < num: 
            b = mid + 1
        else: 
            l = mid - 1
      return -1
  
ar=[int(x) for x in input("Enter numbers in ascending order").split(",")]
print("The list is :",ar)

num=int(input("Enter the number to be searched:"))

res=binarysearch(ar,0,len(ar)-1,num)

if res== -1:
     print(num,"is not present in the array") 
else:
     print(num,"is present at index ",res)
   
