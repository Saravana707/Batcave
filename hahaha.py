a=input('enter no : ')
b=input('enter no : ')
a1=list(a)
b1=list(b)
for i in a:
    for j in b:
        if i==j:
            a1.remove(i)
            b1.remove(j)
            break
count=len(a1)+len(b1)
q=[]
a=['Friend','Lover','Attraction','Marriage','Enemy','Sister']
while len(a)!=1:
    if count>len(a):
        f=count%len(a)
    elif count==len(a):
        f=len(a)
    elif count<len(a):
        f=len(a)-count
    q=a[f:]
    if len(q)==len(a):
        q=[]
    p=a[:f-1]
    q=q+p
    a=q
    l=a
    if len(a)==1:
        break
print('Relationship : ',a[0])
