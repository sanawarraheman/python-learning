"""
python function is a code which call on specific events like click, on change in input etc
and also to reduce number of line of repeated code we use function
"""

def  cylinder_volume(radius, height=1) :
    print('radius', radius)
    print('height', height)
    volume = 3.14*(radius**2)*height
    return volume

r=5
h=10
print(cylinder_volume(r))

def print_pattern(n=5):
    '''
    :param n: Integer number representing number of lines
    to be printed in a pattern. If n=3 it will print,
      *
      **
      ***
    If n=4, it will print,
      *
      **
      ***
      ****
    Default value for n is 5. So if function caller doesn't
    supply the input number then it will assume it to be 5
    :return: None
    '''
    # we need to run two for loops. Outer loop prints patterns line by line
    # where as inner loop print the content of that specific lines
    
    for i in range(n):
        s=''
        for j in range(i+1):
            s=s+"*"
        print(s,j)
        
# def test(n=5):
#         '\n'.join('*' * (i+1) for i in range(n)) 
# print(test(4))
        
print(print_pattern(6))
