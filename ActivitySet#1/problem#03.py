hrs = input("Enter Hours:")
rate=input("Enter Rate:")
pay=float(hrs)*float(rate)
print("Pay:",pay)


hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter rate:")
r=float(rate)
if h>40.0:
    ot=(h-40.0)*(r*1.5)
    pay=40*r+ot
    print(pay)
else:
    pay=h*r
print(pay)
    