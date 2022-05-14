# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
a=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
       continue
    count=count+1
    b=float(line[21:])
    a=b+a
    average=a/count
print("Average spam confidence:",average)        
