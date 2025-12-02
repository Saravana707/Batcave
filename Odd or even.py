import random

class error(Exception): # Exception class for error handling
    pass
def cal():
    while True:
        try:
            num=random.randint(0,10)
            num1=int(input("Enter the number: "))
            if(num1 not in range(0,11)):
               raise error
            else:
               break
        except Exception:
               print("Enter a valid value!")
    print("I enter {}".format(num))
    return num, num1

#*****************BATTING AND BOWLING*********************#

def game1():# Player batting and Computer bowling
    sum =0
    while(True):
        num , num1 = cal()
        if num == num1:
           print("You are out\nYour score is {}".format(sum))
           break
        elif num1==0:
           sum+=num
           print("Your score is {}".format(sum))
        else:
            sum+=num1
            print("Your score is {}".format(sum))
    sum1 =0
    while(True):
        num, num1 = cal()
        if(num1 == num):
            print("I am out\nMy Score is {}".format(sum1))
            if(sum1==sum):
                print("Its a draw")
                print("Our scores are {}".format(sum))
            elif(sum>sum1):
                print("You won, Your score is {} and My score is {} ".format(sum,sum1))
            break
        elif num==0:
            sum1+=num1
            print("My score is {}.".format(sum1))
        else:
            sum1+=num
            print("My score is {}.".format(sum1))
        if sum1 > sum:
            print("I won. My Score is {} and Your score is {}".format(sum1, sum))
            return

def game2():# Computer batting and Player bowling
    sum =0
    while(True):
        num , num1 = cal()
        if num == num1:
           print("I am out\nMy score is {}".format(sum))
           break
        elif num==0:
           sum+=num1
           print("My score is {}".format(sum))
        else:
            sum+=num
            print("My score is {}".format(sum))
    sum1 =0
    while(True):
        num, num1 = cal()
        if(num1 == num):
            print("You are out\nYour Score is {}".format(sum1))
            if(sum1==sum):
                print("Its a draw")
                print("Our scores are {}".format(sum1))
            elif(sum>sum1):
                print("I have won, My score is {} and Your score is {} ".format(sum,sum1))
            break
        elif num1==0:
            sum1+=num
            print("Your score is {}.".format(sum1))
        else:
            sum1+=num1
            print("My score is {}".format(sum1))
        if sum1 > sum:
            print("You have won. Your Score is {} and My score is {}".format(sum1, sum))
            break

#***************************BATTING AND BOWLING**********************************#

print("So we are going to chose which person is going to chose odd or even by tossing a coin")
print("\n")
temp=random.randint(1,2)
toss=0          #the computer 
toss2=0   #the player
oddev=0

#********INPUT FOR TOSSING THE COIN*******


if temp==1:
    print("I am going to ask for the toss")
    temp0=random.randint(1,2)
    if temp0==1:
        print("I Choose Heads")
        toss=1 #heads 1 Tails 2
        toss2=2
    else:
        print("i choose tails")
        toss=2
        toss2=1
else:
    while True:
        try:
            temp1=int(input("What are you going to choose heads(1) or tails(2) :"))
            if temp1!=1 and temp1!=2:
                raise error
            else:
                if temp1==1:
                    toss2=1
                    toss=2
                else:
                    toss2=2
                    toss=1
                break
        except Exception:
            print('Choose an appropriate an answer')


#******INPUT FOR TOSSING THE COIN******


#--------------TOSSING - THE - COIN------------------------------------#


ht=['Heads','Tails']
print("Tossing the coin")
temp2=random.randint(1,2)
if temp2==toss:
    print("Its {}, so i win.".format(ht[toss-1]))
else:
    print("Its {}, so you win".format(ht[toss2-1])) 
    oddev=1



#--------------TOSSING - THE - COIN------------------------------------#



#*****************CHOOSING ODD OR EVEN ******************************#


if oddev==0: #the computer won
    temp4=random.randint(1,2)
    if temp4==1:
        print("I choose odd")
        oddev=2 # Comp - odd || Player - even
    else:
        print("I choose even")
        oddev=1  #Comp - even || Player - odd

else:  #Player won
    while(True):
        try:
            temp5=int(input("Enter what do you want odd(1) or even(2)"))
            if(temp not in [1,2]):
                raise error
            else:
                break
        except Exception:
            print("Enter a valid number")
    if temp5==2:
        oddev=2
    else:
        pass


#*****************CHOOSING ODD OR EVEN ******************************#


chose=1
num , num1 = cal()
num2=num+num1
if num2%2==0:
    print("Its even")
    if oddev==1:
        chose=2   # COMPUTER WON THE ODD OR EVEN
    else:
        pass      #PLAYER WON ODD OR EVEN
else:
    print("Its odd")
    if oddev==2:
        chose=2    #COMPUTER WON ODD OR EVEN
    else:
        pass      #PLAYER WON ODD OR EVEN


#*************************G.A.M.E*********************************#

if chose==2: # COMPUTER WON
    dept=random.randint(1,2)
    if dept==2:
        print("I choose batting\nSo you are bowling")     #COMPUTER BATTING AND PLAYER BOWLING
        game2()
    else:
        print("I choose bowling\nSo you are batting")     #COMPUTER BOWLING AND PLAYER BATTING
        game1()

else:     # PLAYER WON
    while True:
        try:
            dept=int(input("Enter what are you going to choose Batting(1), Bowling(2) : "))
            if(dept not in [1,2]): 
                raise error
            else:
                if dept == 1:
                    print("You have chosen Batting\nSo I am bowling")
                    game1()
                else:
                    print("You have chosen Bowling\nSo I am batting")
                    game2()
            break
        except Exception:
               print("Enter a valid option!")


#**************************G.A.M.E*******************************#
        


        





    
    
    
