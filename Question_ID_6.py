'''The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
* * * * * * * C O M P L E T E D * * * * * * '''

sumOfSquares = 0
for i in range(1,101):
    sumOfSquares+=(i*i)
squareOfSums = 0
for j in range(1,101):
    squareOfSums+=j
squareOfSums=squareOfSums*squareOfSums

print(squareOfSums-sumOfSquares)
