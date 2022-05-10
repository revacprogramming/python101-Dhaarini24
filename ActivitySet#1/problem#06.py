def computepay(hours, rate):
    return(hours,rate)
    if hours>40:
       reg=hours*rate
       ot=(hours-40.0)*(rate*0.5)
       p=reg+ot
    else:
       p=hours*rate
    return p
print("Pay",p)

hrs = input("Enter Hours:")
h=float(hrs)
rate= input("enter rate:")
r=float(rate)
p = computepay(h,r)
print("Pay", p)