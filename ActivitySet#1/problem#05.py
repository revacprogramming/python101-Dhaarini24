def computepay(hours, rate):
    if hours>40:
       #reg=hours*rate
       ot=(hours-40.0)*(rate*1.5)
       pay= 40*r+ot
    else:
       pay=hours*rate
    return pay
hrs = input("Enter Hours:")
h=float(hrs)
rate= input("enter rate:")
r=float(rate)

p= computepay(h,r)
print("Pay", p)