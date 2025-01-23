expenses = [1200, 1300, 1400]

total = 0

for expense in expenses: 
    total= total + expense
    
print(total) # 3900

key_location=  'chair'
locations=['chair', 'table', 'sofas']

for key in locations : 
    if key == key_location:
        print(f'key found on {key}')
        break # break use
    else:
        print('key not found')
        
        
# print odd number 0 to 10

for i in range(11): 
    if i%2==0:
        continue # continue
    print(i)
    
    
# while loop - in for loop numbers are adding and shown serially automatically but here we have to add manually
n=0

while n<=10:
    print(n)
    n=n+1
    
# range() function
print(range(1,11))
print(list(range(1,11)))
for i in range(1,11):
    print(i)
    
    
# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message

for i in range(5):
    print(f'{i+1} miles keep moving')
    tired = input('Are you tired')
    if tired == 'yes':
        break
    if i == 4:
        print('Hurray you just finish the race')
    else:
        print(f'You run to end but you can try later {i+1} km acheived')