a=input('Enter name : ')
b=input('Enter name : ')
c=a
d=b
a=''
b=''
for i in c:
    if i.isalpha():
        a+=i.lower()
for i in d:
    if i.isalpha():
        b+=i.lower()
a1=list(a)
b1=list(b)
for i in a:
    for j in b:
        if i==j and i in a1 and i in b1:
            a1.remove(i)
            b1.remove(i)
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
        f=count-len(a)
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
