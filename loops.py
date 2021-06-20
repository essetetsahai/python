#LOOPS AND ITERATION
print('5.1--Loops and Iterations')

#create loop that subtracts 1 for n > 0

n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
print(n)

#5.2 Definite LOOPS - For LOOPS

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

#definite loop with strings

friends = ['Joseph', 'Glenn', 'Sally']
for i in friends:
    print ('Happy New Year:', i)
print('Done!')

#5.3 Finding the Largest Value
print("Finding the Largest Value")
largest_so_far = -1
print('Before', largest_so_far)

for num in [9, 41, 12, 3, 71, 15]:
    if num > largest_so_far:
        largest_so_far = num
    print(largest_so_far, num)

print('After', largest_so_far)

#Loop Idioms
print('5.4')
print('Loop Idioms')

#Count
cnt = 0
print('Before', cnt)
for thing in [9, 41, 12, 3, 74, 15]:
    cnt = cnt + 1
    print(cnt, thing)
print('After:', cnt)

#Totaling values in series

total = 0
print('Before', total)

for thing in [9,43,32,3,56,15]:
    total = thing + total
    print ('thing=', thing, 'total=', total)
print('After', total)

#Finding the Average in a Loop

print('Finding Average')

cnt = 0
sum = 0
print('Before', 'Count=', cnt, 'Sum=', sum)

for value in [9, 34, 12, 54]:
    cnt = cnt + 1 #counts each value
    sum = sum + value #calculates running sum
    print(cnt, sum, value)
print('After', 'Count=', cnt, 'Sum=', sum, 'Avg=', sum/cnt)

#Filtering in Loops
print('Filtering in Loops')

print('Before')
for value in [23, 9,34, 45, 19, 56]:
    if value > 20:
        print('You got a large number there', value)
print('All done')

#Search Using Boolean Variable
print('Boolean Variable Search')

fnd = False
print('Before', fnd)
for value in [9, 34, 8, 3, 24, 15]:
    if value == 3:
        fnd = True #if 3 is in subset change value of fnd to True
    print(value, fnd)
print('Done:', 'Found 3?', fnd)

#Finding the smallest value
print('Findig the smallest value')
print('')

sml = None               #starting point is 'None' for comparison
print('Before: Smallest value', sml)
for value in [9, 34, 8, 3, 24, 15]:
    if sml is None:     #if the smallest so far is empty/ there's nothing
        sml = value     #then assign the first value(9) as the smallest - this condition is true only for the first value, so it will only run for the first loop
    elif value < sml:   #the loop that is evaluated for all values after the first value because sml has been assigned the first value so it will not be 'none', so skips
        sml = value     #compare value to smallest value so far, if value < sml, then assign sml = that value
    print(sml, value)

print('After:', 'Smallest value =', sml)

#Worked Exercise
print('')
print('Worked Ex 5.1')
print('')

num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'Done':
        break           #exit the rest of the loop if input = done
    fval = float(sval)  #convert input value to float
    print(fval)
    num = num + 1       #count for every input
    tot = tot + fval    #running sum for every input

print('All done')
print('total= ', tot, ' count= ', num, ' avg= ', tot/num)
print('')
print('What if you type someting other than a number or done?')
num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'Done':
        break           #exit the rest of the loop if input = done
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue    #go back to top of loop
    print(fval)
    num = num + 1       #count for every input
    tot = tot + fval    #running sum for every input

print('All done')
try:
    print('total= ', tot, ' count= ', num, ' avg= ', tot/num)
except:
    print('Bad Data')

#Exercise 5.2
#Repeatedly prompt user for int numbers unitl user enters done.
#Once done is entered, print out largest and smallest of numbers.
#If user enters invalid input catch it with try/except

print('')
print('Ex 5.2')

sml = None
lrg = None
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        intval = int(inp)
        if lrg is None:
            lrg = intval
        elif intval > lrg:
            lrg = intval
        if sml is None:
            sml = intval
        elif intval < sml:
            sml = intval
    except:
        print('Invalid input')
        continue
print('All done')


print('Maximum is ', lrg)
print('Minimum is ', sml)
