row = int(input())
col = row * 3 
c1 = "-"
c2 = ".|."
for i in range(int(row / 2)):
    print((i*c2).rjust(int(col/2)-1,c1)+c2+(i*c2).ljust(int(col/2)-1,c1))
    
print("WELCOME".center(col, c1))

for j in range(int(row/2)-1,-1 ,-1):
    print((j*c2).rjust(int(col/2)-1,c1)+c2+(j*c2).ljust(int(col/2)-1,c1))
