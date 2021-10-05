'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
* * * * * * * C O M P L E T E D * * * * * * * '''

Multiple = 0
ListOfAllMultiples = []
for i in range(100,1000):
    for j in range(100,1000):
        Multiple = i*j
        ListOfAllMultiples.append(Multiple)
ElementToBeAdded = 0
ReveresedList = []
for k in range(len(ListOfAllMultiples)-1,0,-1):
    ElementToBeAdded = ListOfAllMultiples[k]
    ReveresedList.append(ElementToBeAdded) 
ListOfPalindromes = []
def PalindromeCheck(x):
    if x[0]==x[len(x)-1]:
        if x[1]==x[len(x)-2]:
            if x[2]==x[len(x)-3]:
                ListOfPalindromes.append(x)
    return(0)
IntegerToString = ""
for p in ReveresedList:
    IntegerToString = str(p)
    if len(IntegerToString)>5:
        PalindromeCheck(IntegerToString)
print("Largest Palindrome is ",ListOfPalindromes[2])
#huh? why tf do i need this - print(ListOfPalindromes)
