n= input('Enter the number')

n=int(n)

if n%2==0:
    print('Number is Even')
else: 
    print('Number is Odd')
    # simaple way for above code
    message = 'Number is Even' if n%2==0 else 'Number is Odd'
    print(message)
    
    print(4==4) # true
    print(2>3) # false
    print(2<3) # true
    print(2>=2) # true
    print(4<=4) # true
    print(3>2 and 3>1) #true
    print(3>2 and 3>4) # false
    print(3>2 or 3>4) # true
    print(3>2 or 3>4 or 4<5) # true
    print(2>3)
    
    indian = ['samosa', 'jalebi', 'pakoda']
    pakistani = ['nihari', 'paya', 'karahi']
    bangladeshi = ['panta bhat', 'chorchori', 'fuchka']
    
    dish = input('Enter dish name')
    
    if dish in indian: 
        print(f'{dish} is India')
    elif dish in pakistani:
        print(f'{dish} is Pakistani')
    elif dish in bangladeshi:
        print(f'{dish} is Bangladeshi')
    else: 
        print(f'{dish} is not in list try indian bangladeshi and pakistani')
        