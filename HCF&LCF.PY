print("Enter Three Numbers: ", end="")
no = int(input())
nt = int(input())
number=int(input())

a = no
b = nt
c=number

while b!=0:
    temp = b
    b = a%b
    a = temp
    c!=b%c
    temp=c
    
hcf = a
lcm = int((no*nt)/hcf)

print("\nLCM (" + str(no) + ", " + str(nt) + ", " + str(number) + ") = ", lcm)
print("HCF (" + str(no) + ", " + str(nt) + " ," + str(number) + ") = ", hcf)
