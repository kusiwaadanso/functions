#delta determines if roots will be real or not


#function for delta
def delta(a,b,c):
    delta=b**2-4*a*c
    return delta
   
#function for root extration

def root_extraction(a,b,delta):
    if delta<0:
        return 'the equation has no real roots'
    elif delta==0:
        x1=(b**2-delta)/(2*a)
       return x
elif delta>0:
x1=(-b-delta**(0.5))/(2*a)
x2=(-b+delta**(0.5))/(2*a)
return (x1,x2)












