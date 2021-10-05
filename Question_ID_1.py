'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
* * * * * * * C O M P L E T E D * * * * * * '''

list_of_three = []
list_of_five = []
list_of_all = []
list_of_both = []
for i in range(0,1000):
    if i%3==0:
        list_of_three.append(i)
        list_of_all.append(i)
for k in range(0,1000):
    if k%5==0:
        list_of_five.append(k)
        list_of_all.append(k)
for o in range(0,1000):
    if o%5==0 and o%3==0:
        list_of_both.append(o)
sum_of_both = 0
sum_of_all = 0
for p in list_of_both:
    sum_of_both+=p
for l in list_of_all:
    sum_of_all+=l
print(list_of_both)
print(list_of_three)
print(list_of_five)
print(list_of_all)
print("Sum is :",sum_of_all-sum_of_both)
