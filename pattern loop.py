#python program to print a triangle of numbers   
#output based questions

for i in range(1,10): # for choosing a number from 1 to 9, 9 itterations will take place
   for j in range(i):   #for each iteration of i this range changes.
      print(i, end=' ')  # end=" " to make iderated values to fall in the same line
    
   print('')
      
""" Explanation:
ranges of j:
1. 0 (one iteration) so 1 is printed once (corresponding value of i)
2. 0,1 (2 iteration) so 2 is printed twice
3. 0,1,2 (3 iteration) so 3 is printed thrice
4. 0,1,2,3 (4 iteration) so 4 is printed 4 times
5. 0,1,2,3,4 (5 iteration) so 5 is printed 5 times
6. 0,1,2,3,4,5 (6 iteration) so 6 is printed 6 times
7. 0,1,2,3,4,5,6 (7 iteration)so 7 is printed 7times
8.  0,1,2,3,4,5,6,7 (8 iteration)so 8 is printed 8 times
9.  0,1,2,3,4,5,6,7,8 (9 iteration)so 9 is printed 9 times

"""
