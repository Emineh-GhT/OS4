
n=int (input("tedad jomalat donbale ra vared konid ? \t"))
for i in range(0,1) :
    f=[0,1]
for i in range(2,n+1):
    f.append(f[i-1]+f[i-2])
print ("*"*(5*n)) 
print(f)
print ("*"*(5*n))