# triangle area 1/2 * base * height

base = 9
height = 3

area_of_triangle = (1/2)*base*height #13.5
print(area_of_triangle) # type: ignore

# round method to make decimal points in round digits like round(number to be round, how many decimal points)
rounded = round(area_of_triangle, 0) # 13.5 converted to 14
print(rounded)

# python do multiplication first
10+2*3 # 16

# if you want addition first then use ()
(10+2) * 3 # 36
type(rounded)

type(2.5)
#<class 'float'>
foo=2.5e-3
foo
#0.0025
0x22 # 16 * (2+2)
#34
0x12 # 16 * (1+2)
#18
c1=2+3j
type(c1)
#<class 'complex'>
c2=3-4j
c1+c2
#(5-1j)
format(5, 'b') # '101'
# 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 5

# Exercise
# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total
#    area using python and print it
length=92
width=48.8
area=length*width
print("area of football field:",area) # Ans: 4489.599999999999

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#    and you gave shopkeeper 20 dollar.
#    Find out using python, how many dollars is the shopkeeper going to give you back?
num_packets=9
cost_per_packet=1.49
total_cost=num_packets*cost_per_packet
money_paid=20
cash_back=money_paid-total_cost
print("Cash back:",cash_back) # Ans: 6.59

# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square
length=5.5
area=length**2 # area of square is length power 2
cost=area*500
print("total cost for bathroom tiles replacement:",cost) # Ans: 15125.0

# 4. Print binary representation of number 17
num=17
print('Binary of number 17 is:',format(num,'b')) # Ans: 10001