from math import sqrt

a,b,c=eval(input('Enter coefficients'))

disc=b*b-4*a*c

if disc>0:
    x1=(-b+sqrt(disc))/2*a
    x2=(-b+sqrt(disc))/2*a
    print(f'Solution: {x1},{x2}')

else:
    print('No solution')


