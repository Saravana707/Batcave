import random
import time
class error(Exception):
    pass
def game(a,b):
    c=0
    d=0
    if a>b:
        while True:
            while True:
                try:
                    a=int(input("Enter No : "))
                    if a>10 or a<0:
                        raise error
                    break
                except Exception:
                    print("Enter a valid number from 0 to 10")
            b=random.randint(0,10)
            print("I choose",b)
            if a==b:
                print("You are out")
                print("The Target is",c)
                break
            elif a==0:
                c+=b
                print("Your score is ",c)
            else:
                c+=a
                print("Your score is ",c)
        print("Now I am batting")
        while True:
            while True:
                try:
                    a=int(input("Enter No : "))
                    if a>10 or a<0:
                        raise error
                    break
                except Exception:
                    print("Enter a valid number from 0 to 10")
            b=random.randint(0,10)
            print("I choose",b)
            if a==b:
                print("I am out")
                if d==c:
                    print("Its a tie. We both have scored {}".format(d))
                    break
                elif c>d:
                    print("You won. Your Score is {} and My score is {}".format(c,d))
                    break
                else:
                    pass
            elif b==0:
                d+=a
                print("My score is {} | The target is {}".format(d,c))
            elif d+b>c:
                print("I won")
                print("My score is {} and Your score is {}".format(d+b,c))
                break
            else:
                d+=b
                print("My score is {} | The target is {}".format(d,c))
    else:
        while True:
            while True:
                try:
                    a=int(input("Enter No : "))
                    if a>10 or a<0:
                        raise error
                    break
                except Exception:
                    print("Enter a valid number from 1 to 10")
            b=random.randint(0,10)
            print("I choose",b)
            if a==b:
                print("I am out")
                print("The Target",c)
                break
            elif b==0:
                c+=a
                print("My score is",c)
            else:
                c+=b
                print("My score is",c)
        print("Now you are batting")
        while True:
            while True:
                try:
                    a=int(input("Enter No : "))
                    if a>10 or a<0:
                        raise error
                    break
                except Exception:
                    print("Enter a valid number from 0 to 10")
            b=random.randint(0,10)
            print("I chose",b)
            if a==b:
                print("You are out")
                if d==c:
                    print("Its a tie. Both our scores are {}".format(d))
                elif c>d:
                    print("I have won the game.My score is {} and your score is {}".format(c,d))
                else:
                    pass
                break
            elif a==0:
                d+=b
                print("Your score is {} | The target is {}".format(d,c))
            elif d+a>c:
                print("You have won.\n Your score is {} and My score is {}".format(d,c))
            else:
                d+=a
                print("Your score is {} | The target is {}".format(d,c))
for i in "Now I am choosing radomly who's gonna ask odd or even....":
    if i=='.':
        time.sleep(0.9)
        print(i,end='')
    else:
        print(i,end='')
print('\n')
temp=random.randint(0,1)
if temp==0:
    print("You can choose")
    while True:
        try:
            y=int(input("Choose odd(1) or even(2) : "))
            if y!=1 and y!=2:
                raise error
            else:
                break
        except Exception:
            print("ENTER A VALID CHOICE!")
    if y==1:
        while True:
                try:
                    temp3=int(input("Enter No : "))
                    if temp3>10 or temp3<0:
                        raise error
                    break
                except Exception:
                    print("Enter a valid number from 0 to 10")
        temp2=random.randint(0,10)
        print("I choose",temp2)
        add=temp2+temp3
        if add%2==0:
            print("The sum is {},its even. So i win".format(add))
            temp=random.randint(0,1)
            if temp==0:
                print("I choose batting")
                game(1,2)
            else:
                print("I choose bowling")
                game(2,1)
        else:
            print("The sum is {},its odd. So you win".format(add))
            while True:
                try:
                    y2=int(input("Enter what are you choosing Batting(1) or Bowling(2) : "))
                    if y2!=1 and y2!=2:
                        raise error
                    else:
                        break
                except Exception:
                    print("ENTER A VALID CHOICE")
            if y2==1:
                print("SO you are batting and I am Bowling")
                game(2,1)
                
            else:
                print("SO i am batting and You are Bowling")
                game(1,2)
    else:
        while True:
                try:
                    temp3=int(input("Enter No : "))
                    if temp3>10 or temp3<0:
                        raise error
                    break
                except Exception:
                    print("Enter a valid number from 0 to 10")
        temp2=random.randint(0,10)
        print("I choose",temp2)
        add=temp2+temp3
        if add%2==0:
            print("The sum is {},its even. So you win".format(add))
            while True:
                try:
                    y2=int(input("Enter what are you choosing Batting(1) or Bowling(2) : "))
                    if y2!=1 and y2!=2:
                        raise error
                    else:
                        break
                except Exception:
                    print("ENTER A VALID CHOICE")
            if y2==1:
                print("SO you are batting and I am Bowling")
                game(2,1)
                
            else:
                print("SO i am batting and You are Bowling")
                game(1,2)
        else:
            print("The sum is {},its odd. So I win".format(add))
            temp=random.randint(0,1)
            if temp==0:
                print("I choose batting")
                game(1,2)
            else:
                print("I choose bowling")
                game(2,1)
else:
    print("I am going to choose")
    temp90=random.randint(1,2)
    if temp90==1:
        print("I choose odd")
        while True:
                try:
                    temp3=int(input("Enter No : "))
                    if temp3>10 or temp3<0:
                        raise error
                    break
                except Exception:
                    print("Enter a valid number from 0 to 10")
        temp2=random.randint(0,10)
        print("I choose",temp2)
        rep=temp3+temp2
        if rep%2==0:
            print("The sum is {},Its even. So you win".format(rep))
            while True:
                try:
                    y2=int(input("Enter what are you choosing Batting(1) or Bowling(2) : "))
                    if y2!=1 and y2!=2:
                        raise error
                    else:
                        break
                except Exception:
                    print("ENTER A VALID CHOICE")
            if y2==1:
                print("SO you are batting and I am Bowling")
                game(2,1)
                
            else:
                print("SO i am batting and You are Bowling")
                game(1,2)
        else:
            print("The sum is {},Its odd. So i win".format(rep))
            temp=random.randint(0,1)
            if temp==0:
                print("I choose batting")
                game(1,2)
            else:
                print("I choose bowling")
                game(2,1)
    else:
        print("I choose even")
        while True:
                try:
                    temp3=int(input("Enter No : "))
                    if temp3>10 or temp3<0:
                        raise error
                    break
                except Exception:
                    print("Enter a valid number from 0 to 10")
        temp2=random.randint(0,10)
        print("I choose",temp2)
        rep=temp3+temp2
        if rep%2==0:
            print("The sum is {},its even. So i win".format(rep))
            temp=random.randint(0,1)
            if temp==0:
                print("I choose batting")
                game(1,2)
            else:
                print("I choose bowling")
                game(2,1)
        else:
            print("The sum is {},its odd. You win".format(rep))
            while True:
                try:
                    y2=int(input("Enter what are you choosing Batting(1) or Bowling(2) : "))
                    if y2!=1 and y2!=2:
                        raise error
                    else:
                        break
                except Exception:
                    print("ENTER A VALID CHOICE")
            if y2==1:
                print("SO you are batting and I am Bowling")
                game(2,1)
                
            else:
                print("SO i am batting and You are Bowling")
                game(1,2)
            
        
        
        
            
            
            
        

            
                
                
            
            
            
            
        
            
        
