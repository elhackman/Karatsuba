#-------------------------------------------------------------------------------
# Name:        Karatsuba Algorithm Implementation
#
# Author:      David Bautista
#
# Created:     01/05/2013
#-------------------------------------------------------------------------------

import math

#Returns the first m digits of a number
def lhalf(c,m):
    return int(str(c)[:m])

#Returns the last m digits of a number    
def rhalf(c,m):
    return int(str(c)[-m:])

def multp(a,b):
    #If the numbers are too small, makes the multiplication directly
    if (0 <= a < 10) or (0 <= b < 10):
        return a*b
        
    elif (type(a) == int) and (type(b) == int) or (type(a) == long) and (type(b) == long):
        #Computing the sign of the result
        zs = int(math.copysign(1,a)*math.copysign(1,b))
        
        #Working with non-signed numbers
        x = str(abs(a))
        y = str(abs(b))
        xl = len(x)
        yl = len(y)
        
        #Making 'm' even
        if max(xl,yl) & 1:
            m = max(xl,yl)+1
        else:
            m = max(xl,yl)
        
        mh = m/2
        
        #Zero-filling strings to fit m-size
        x = x.rjust(m,'0')
        y = y.rjust(m,'0')
            
        x0 = rhalf(x,mh)
        x1 = lhalf(x,mh)

        y0 = rhalf(y,mh)
        y1 = lhalf(y,mh)        

        z0 = multp(x0,y0)
        z1 = multp(x1+x0,y1+y0)
        z2 = multp(x1,y1)
        
        return zs*((z2*(10**m))+((z1-z2-z0)*(10**(mh)))+z0)
        
    #Returns false if it's used a parameter type other than int or long
    else:
        return False