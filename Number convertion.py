class error(Exception):
    pass
ab=["A","B","C","D","E","F"]
while True:
    try:
        a=int(input("From which you want to convert from :\n"
              "1) Decimal \n"
              "2) Binary \n"
              "3) Octal \n"
              "4) Hexadecimal \n"
              "ENTER YOUR CHOICE : "))  
        if a not in [1,2,3,4]:
            raise error
        else:
            break
    except Exception:
        print("Enter a valid option!")
if a==1:
    ans=''
    while True:
        try:
            c=int(input("Enter a decimal number : "))
            b=int(input("What do you want to convert it to :\n"
              "1) Binary \n"
              "2) Octal \n"
              "3) Hexadecimal \n"
              "ENTER YOUR CHOICE : "))          
            if b not in [1,2,3]:
                raise error
            else:
                break
        except Exception:
            if b not in [1,2,3]:
                print("Enter a valid option!")
            else:
                print("Enter a appropriate value")
    if b==1:
        while c!=1:
            ans+=str(c%2)
            c//=2
        ans+="1"
        print("The Binary value is {}".format(ans[::-1]))
    elif b==2:
        while c>8:
            ans+=str(c%8)
            c//=8
        ans+=str(c)
        print("The Octal value is {}".format(ans[::-1]))
    else:
        while c>16:
            if (c%16)>9:
                ans+=ab[(c%16)-10]
            else:
                ans+=str(c%16)
            c//=16
        if c>9:
            ans+=ab[c-10]
        else:
            ans+=str(c)
        print("The hexadecimal value is {}".format(ans[::-1]))
elif a==2:
    ans=0
    b=1
    while True:
        try:
            c=int(input("Enter a binary number : "))
            for i in str(c):
                if i!='0' and i!='1':
                    raise error
            b=int(input("What do you want to convert it to :\n"
              "1) Decimal \n"
              "2) Octal \n"
              "3) Hexadecimal \n"
              "ENTER YOUR CHOICE : "))
            if b not in [1,2,3]:
                raise error
            else:
                break
        except Exception:
            if b not in [1,2,3]:
                print("Enter a valid option!")
            else:
                print("Enter a appropriate value")
    if b==1:
        k=str(c)
        temp=0
        for i in k[::-1]:
            if i=='1':
                ans+=2**temp
            else:
                pass
            temp+=1
        print("The Decimal value is {}".format(ans))
    elif b==2:
        k=[]
        o=str(c)
        ans3=""
        while len(o)>3:
            k.append(o[-3:])
            o=o[:-3]
        if len(o)!=0:
            k.append(o)
        else:
            pass
        for i in k:
            ans2=''
            l=0
            s=0
            for j in i[::-1]:
                if j=="1":
                    s+=2**l
                else:
                    pass
                l+=1
            ans2=str(s)
            ans3+=ans2
        print("The Octal value is {}".format(ans3[::-1]))
    elif b==3:
        k=[]
        o=str(c)
        ans3=""
        while len(o)>4:
            k.append(o[-4:])
            o=o[:-4]
        if len(o)!=0:
            k.append(o)
        else:
            pass
        for i in k:
            ans2=''
            l=0
            s=0
            for j in i[::-1]:
                if j=="1":
                    s+=2**l
                else:
                    pass
                l+=1
            if s>9:
                ans2+=ab[s-10]
            else:
                ans2=str(s)
            ans3+=ans2
        print("The Hexadecimal value is {}".format(ans3[::-1]))
    else:
        pass
elif a==3:
    ans=0
    b=1
    while True:
        try:
            c=int(input("Enter a Octal number : "))
            for i in str(c):
                if int(i)>7:
                    raise error
            b=int(input("What do you want to convert it to :\n"
              "1) Decimal \n"
              "2) Binary \n"
              "3) Hexadecimal \n"
              "ENTER YOUR CHOICE : "))
            if b not in [1,2,3]:
                raise error
            else:
                break
        except Exception:
            if b not in [1,2,3]:
                print("Enter a valid option!")
            else:
                print("Enter a appropriate value")
    if b==2:
        b=str(c)
        k=''
        for i in b:
            if int(i)%2==0:
                if i=="6":
                    k+="110"
                elif i=="2":
                    k+="010"
                elif i=="0" and k!="":
                    k+="0"
                else:
                    k+="100"
            else:
                if i=="1":
                    k+="001"
                elif i=="3":
                    k+="011"
                elif i=="5":
                    k+="101"
                else:
                    k+="111"
        k=k.lstrip("0")
        print("The Binary value is : {}".format(k))
    elif b==1:
        b=str(c)
        k=''
        for i in b:
            if int(i)%2==0:
                if i=="6":
                    k+="110"
                elif i=="2":
                    k+="010"
                elif i=="0" and k!="":
                    k+="0"
                else:
                    k+="100"
            else:
                if i=="1":
                    k+="001"
                elif i=="3":
                    k+="011"
                elif i=="5":
                    k+="101"
                else:
                    k+="111"
        k=k.lstrip("0")
        ans=0
        temp=0
        for i in k[::-1]:
            if i=='1':
                ans+=2**temp
            else:
                pass
            temp+=1
        print("The Decimal value is {}".format(ans))
    elif b==3:
        b=str(c)
        k=''
        for i in b:
            if int(i)%2==0:
                if i=="6":
                    k+="110"
                elif i=="2":
                    k+="010"
                elif i=="0" and k!="":
                    k+="0"
                else:
                    k+="100"
            else:
                if i=="1":
                    k+="001"
                elif i=="3":
                    k+="011"
                elif i=="5":
                    k+="101"
                else:
                    k+="111"
        k=k.lstrip("0")
        c=k
        k=[]
        o=c
        ans3=""
        while len(o)>4:
            k.append(o[-4:])
            o=o[:-4]
        if len(o)!=0:
            k.append(o)
        else:
            pass
        for i in k:
            ans2=''
            l=0
            s=0
            for j in i[::-1]:
                if j=="1":
                    s+=2**l
                else:
                    pass
                l+=1
            if s>9:
                ans2=ab[s-10]
            else:
                ans2=str(s)
            ans3+=ans2
        print("The Hexadecimal value is {}".format(ans3[::-1]))
else:
    ans=0
    b=1
    while True:
        try:
            c=input("Enter a Hexadecimal number : ")
            for i in str(c):
                if i not in ab and int(i)>9:
                    raise error
                else:
                    pass
            b=int(input("What do you want to convert it to :\n"
              "1) Decimal \n"
              "2) Binary \n"
              "3) Octal \n"
              "ENTER YOUR CHOICE : "))          
            if b not in [1,2,3]:
                raise error
            else:
                break
        except Exception:
            if b not in [1,2,3]:
                print("Enter a valid option!")
            else:
                print("Enter a appropriate value")
    c1=c
    k=""
    for i in c1:
        d=0
        if i in ab:
            d=ab.index(i)+10
        else:
            d=int(i)
        if d%2==0:
            if d==2:
                k+="0010"
            elif d==4:
                k+="0100"
            elif d==6:
                k+="0110"
            elif d==8:
                k+="1000"
            elif d==10:
                k+="1010"
            elif d==12:
                k+="1100"
            else:
                k+="1110"
        else:
            if d==1:
                k+="0001"
            elif d==3:
                k+="0011"
            elif d==5:
                k+="0101"
            elif d==7:
                k+="0111"
            elif d==9:
                k+="1001"
            elif d==11:
                k+="1011"
            elif d==13:
                k+="1101"
            else:
                k+="1111"
    k=k.lstrip("0")
    if b==2:
        print("The Binary value is {}".format(k))
    elif b==1:
        temp=0
        for i in k[::-1]:
            if i=='1':
                ans+=2**temp
            else:
                pass
            temp+=1
        print("The Decimal value is {}".format(ans))
    elif b==3:
        k1=k
        k=[]
        o=k1
        ans3=""
        while len(o)>3:
            k.append(o[-3:])
            o=o[:-3]
        if len(o)!=0:
            k.append(o)
        else:
            pass
        for i in k:
            ans2=''
            l=0
            s=0
            for j in i[::-1]:
                if j=="1":
                    s+=2**l
                else:
                    pass
                l+=1
            ans2=str(s)
            ans3+=ans2
        print("The Octal value is {}".format(ans3[::-1]))
    else:
        pass
        
        
        
                

                
    


        
        
        
        
