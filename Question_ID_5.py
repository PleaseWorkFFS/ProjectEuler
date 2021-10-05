'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''


'''KEEP TRACK
1[o] 2[o] 3[o] 4[o] 5[o] 6[o] 7[o] 8[o] 9[o] 10[o] 11[o] 12[o] 13[o] 14[o] 15[o] 16[o] 17[o] 18[o] 19[o] 20[o]
* * * * * * C O M P L E T E D * * * * * * * '''

for i in range(230000000,233000000):
    if i%19==0:
        if i%17==0:
            if i%15==0:
                if i%13==0:
                    if i%11==0:
                        if i%14==0:
                            if i%6==0:
                                if i%4==0:
                                    print("The smallest number divisible by all no. 1-20 : ",i)
