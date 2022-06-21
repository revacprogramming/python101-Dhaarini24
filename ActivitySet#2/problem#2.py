def add(a, b):
    q=int(a)
    p=int(b)
    m = q+p
    return m
  
def output(p,q,m):
    print('the   sum of a and b is ',m)   


def main():
    a,b = input_two_numbers()
    sum = add(a, b)

    output( a,b,sum)
 
name=input('whats the operation?')
if name == 'addition':
    main()











