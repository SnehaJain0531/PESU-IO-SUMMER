
#Function for question 1 
def qn1():
    inp = input("Comma Separated numbers:")
    l1 = inp.split(",")
    t1 = tuple(l1)
    print('List generated : ',l1)
    print('Tuple generated: ',t1)

#Function for question 2
def qn2():
    numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
                399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
                815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
                958,743, 527 ]
    for i in numbers:
        if i == 237:
           break;
        elif i % 2 == 0:
            print(i,end=' ')

#Function for question 4
def qn4():
    num=input("Enter a number:")
    num=int(num)
    m=num
    s=0
    while(m):
      rem = m % 10
      s = s+rem
      m=m//10
    print('Th sum of digits of',num,'=',s)

#Function for question 5
def qn5():
    st=input("Enter the string to be checked")
    try:
      st1= float(st)
      print(st,'is Numeric')
    except (ValueError,TypeError):
      print(st,'is not Numeric')

#Answer for Binary Search is commited in different file 
