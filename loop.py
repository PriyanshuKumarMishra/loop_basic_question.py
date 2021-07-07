### sum print ###

# a=50
# b=0
# while a<60:
#     c=int(input("enter the number:"))
#     b=b+c
#     a+=1
# print(b)


# a=50
# b=0
# while a-60:
#     c=int(input("enter the number:"))
#     b=b+c
#     a+=1
# print(b)


# a=int(input("enter the number: "))
# b=0
# x=0
# while b<a:
#     c=int(input())
#     b+=1
#     x+=c
# print(x)


#######################################
#### sum and average of the element #####

# a=3
# b=1
# c=0
# e=0
# while b<=a:
#     p=int(input())
#     c+=p
#     e=c/a
#     b+=1
# print(c)
# print(e)

#######################
# ### prime number ####

# a=int(input())
# f=0
# b=2
# while b<=a/2:
#     if a%b==0:
#         f=1
#         break
#     b=b+1
# if f==0:
#     print("prime")
# else:
#     print(" not prime number")


# a=int(input(" "))
# b=2
# while b<a:
#     if a%b==0:
#         print("no")
#         break
#     b+=1
# else:
#     print("yes")


# a=20
# while a<=100:
#     print(a)
#     a+=2


# a=7
# while a<100:
#     print(a)
#     a+=7


# a=30
# b=0
# while a<=40:
#     b=a+b
#     a=a+2
# print(b)


# a=12
# b=0
# while a<=420:
#     b=a+b
#     a+=1
# print(b)


# a=30
# b=0
# while a<420:
#     if a%8==0:
#         b=a+b
#         print("a",a)
#     a+=1
# print(b)

#######################
#### average print ####

# a=1
# b=0
# while a<=11:
#     c=int(input())
#     b=b+c
#     d=b/11
#     a+=1
# if d%5==0:
#     print("yes")
# else:
#     print("no")
# print(d)

#################################################
#### odd number pisitive even number negative ####

# a=1
# b=2
# while a<=100:
#     print(a)
#     print(b*(-1))
#     a+=2
#     b+=2

######################
#### gussing game ####

# a=5
# b=1
# c=0
# while b<=3:
#     c=int(input("enter the number: "))
#     b+=1
#     if a==c:
#         print("won")
#         break
#     else:
#         print("try again")
# else:
#     print("you lost the game ")
      

# a=5
# b=1
# c=0
# while b<=3:
#     c=int(input("enter the number: "))
#     b+=1
#     if a==c:
#         print("won")
#         break
#     elif a>c:
#         print("chota hai try again")
#     else:
#         print("bada hai try again")
# else:
#     print("you lost the game ")


# a=1
# b=0
# while a<=50:
#     a,b=b,a
#     c=a+b
#     print(c)
#     a+=1                                                                                                             


# c=0
# d=1
# while c<3:
#     c=c+1
#     d=d*c
#     print(c,d)
# else:
# #     print(c,d)


# i = 0
# while(i<5):
#     j = 0
#     while(j<5): #loop2
#         if (j > 3): 
#             break 
#         else:
#             print ("*") 
#         j = j + 1    
#     print ('')
#     i = i + 1
 

# x = 0
# while(x<7):
#     if (x == 3 or x==5):
#         x = x + 1
#         continue
#     print(x)
#     x = x + 1 


#####################################################
#### 2 number multiply without use multiply sign ####

# a=int(input("enter the number: "))
# b=int(input("enter the number: "))
# c=0
# co=0
# while c<b:
#     co=co+a
#     c+=1
# print(co)


################################
#####   Fibonacci  Series  #####

# a=int(input())
# b=0
# c=1
# d=0
# while d<=a:
#     # print(b)
#     e=b+c
#     b=c
#     c=e
#     d+=1
# print(b)


###################################################
##### star pattern difference difference type #####

# a=int(input())
# b=0
# while b<+a:
#     print("  "*(a-2)+"  *"*(a-b))
#     b+=1

# a=int(input())
# b=0
# while b<+a:
#     print("  "*(a+b)+"  *"*(a-b))
#     b+=1

# a=int(input())
# b=0
# while b<+a:
#     print("   "*(a-b)+"*  "*(a-b))
#     b+=1

# a=int(input( ))
# b=1
# while b<=a:
#     print(" "*(a-b)+"* "*b)
#     b+=1
   
# a=int(input())
# b=1
# while b<+a:
#     print(" "*(a-b)+" *"*a)
#     b+=1

# a=int(input())
# b=0
# while b<+a:
#     print("  "*(a-b)+"  *"*(a-b))
#     b+=1

# a=int(input( ))
# b=1
# while b<=a:
#     print(" "*(a-b)+"* "*b)
#     b+=2


##########################################################
### odd number is positive and even number is negative ###

# a=1
# b=2
# while a<=100:
#     print(a,b*(-1))
#     a+=2
#     b+=2


################################
### this code is hppy number ###

# num=int(input())
# n=num
# sum=0
# while sum!= 1 and sum!=4:
#     sum=0
#     while n>0:
#         digit=n%10
#         sum=sum+digit**2
#         n=n//10
#     n=sum
# if sum==1:
#     print("h")
# else:
#     print("n")


#####################
##### Factiriol #####

# a=int(input())
# b=1
# for i in range (a):
#     b=b*(i+1)
# print(b)


#########################################
#### This code is  String palindrome ####

# x=input(" ")
# b=""
# for i in x:
#     b=i+b
# if x==b:
#     print("y")
# else:
#     print("n")


##########################    
#### R pattern print  ####

# x=4
# y=1
# while y!=5:
#     if y==1:
#         print("* "*x)
#         print("* "," "*2,"*")
#         print("* "*x)
#     else:
#         print("*"," "*(y-2),"*")
#     y+=1
 

#########################
### table print 2*1=2 ###

# a=int(input())
# for i in range (1,11):
#     print(str(a), "*", str(i), "=", str(i*a))

# a= int(input())
# for i in range (1, a+1):
#     for j in range (1,11):
#         print(i*j)
# print()


#########################################
###### odd and even number ##########
# a=1
# while a<=100:
#     a+=1
#     if a%2==0:
#         print(a,"even")
#         if a==100:
#             a-=99
#     else:
#         print(a,"odd")
#     a+=1


##############################################
#### odd even print (first even then odd) ####

# a=2
# while a<=200:
#     if a<=100:
#         if a%2==0:
#             print(a)
#     else:
#         if a%2!=0:
#             print(a-100)
#     a+=1 


########################################################################
#### first  pehle ke three number even then baad ke three number odd ####

# a=int(input())
# f=a
# v=f
# i=0
# while a>0:
#     a-=1
#     if a%2==0:
#         print(a,end=' ')
#         if f-a==5:
#             break
#         elif f-a==6:
#             break
# print()
# while f>0:
#     f+=1
#     if f%2!=0:
#         print(f,end=' ')
#         if f-v==5:
#             break
#         elif f-v==6:
#             break
# print()


########################################
### without use number print 1 to 10 ###

# a=ord("A")
# b=ord("J")
# c=ord("@")
# x = a-c
# while a <= b:
#     print(a-c)
#     a+=x


##################################
####### integer palindrome #######

# x=int(input())
# s = str(x)
# rs = "".join(list(reversed(s)))
# if rs != s:
#     print (False)
# else:
#     print(True)
