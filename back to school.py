l=list(input()+' ')
m=0
c=''
for i in range(len(l)):
    if l[i]!=' ':
        c=c+l[i]
    else:
        if m<int(c):
            m=int(c)
        c=''

print(m)        