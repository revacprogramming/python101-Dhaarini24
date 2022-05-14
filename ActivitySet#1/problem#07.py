text = "X-DSPAM-Confidence:    0.8475"
a= text.find(":")
#print(a)
s= text[a+4:]
value=float(s)
print(value)           