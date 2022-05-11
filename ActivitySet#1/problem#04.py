score = input("Enter Score: ")
i=float(score) 
if i>=0.9 and i<=1.0:
     print("A")
elif i>=0.8 and i<0.9:
     print("B")
elif i>=0.7 and i<0.8:
     print("C")
elif i>=0.6 and i<0.7:
     print("D")
elif i<0.6 and i>=0.0:
     print("F")
else:
    print("error, print the number in the suitable range")

