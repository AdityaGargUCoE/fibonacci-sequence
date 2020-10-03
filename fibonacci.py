nterms = int(input("enter the number of terms:"))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("enter the valid terms")
elif nterms == 1:
    print("fibonnaci series upto", nterms, ":")
    print(n1)
else:
    print("fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1