hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter rate:")
r=float(rate)
if h>40.0:
    reg=h*r
    ot=(h-40.0)*(r*0.5)
    pay=reg+ot
    print(pay)
else:
    pay=h*r
print(pay)
    
