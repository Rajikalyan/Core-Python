# x=10
# if x==15:
#     print("welcome")
# else:
#     print("exit")

# take a input of marks
# >=90 and <=100 ---> grade A
# >=80 and <=89 ----> grade B
# >=60 and <=79 ----> grade C
# >=35 and <=59 ---> grade D
# <35 ----> fail




# mark = int(input("Enter Your Marks: "))
#
# if mark>=90 and mark<=100:
#     print("Grade: A")
# elif mark>=80 and mark<=89:
#     print("Grade: B")
#
# elif mark>=60 and mark<=79:
#     print("Grade: C")
#
# elif mark>=35 and mark<=59:
#     print("Grade: D")
#
# else:
#     print("Fail")


# print("""
#
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
#
# """)
#
# choice = int(input('Enter Your Choice: '))
# if choice==5:
#     print(quit())
# n1 = int(input("Enter No1: "))
# n2 = int(input("Enter No2: "))
# if choice==1:
#     print(n1+n2)
#
# elif choice==2:
#     print(n1-n2)
#
# elif choice==3:
#     print(n1*n2)
#
# else:
#     print(n1/n2)

#x = int(input("enter value"))
#if x>=2:
  #  print("x,type of x")
#elif x<=1:
   # print("program exist")
#else:
   # print("enter new number")

#x = int(input("enter number:"))
#if x<=0:
 #      print("x,type(x)")
#elif x>=1:
 #       print("x+1")
#else:
 #      print("x*0")



#if True and True :
  #  print("logical and True1")


#varibles if x = 10 ,x is variable,which stores address of value,its like char anything,some times its also
# identifier,it should start with letter or _(underscore),3 type of varibales int,float,complex.

#x=10
#print(x)

#x=int(input("enter number :"))
#print(x,type(x))

#x=float(input("enter number :"))
#print(x,type(x))

########################operators 7 type of operators are there###########
#1#arithematic operators##
# +,_,*,/,%,%%
#x=10
#y=12
#print(x+y)
#x=10
#y=12
#print(x//y)

#2# assignment operators##
# =,+=,-+,*=,/=,%=,**=,//=

#x=(5)
#x//=5
#print(x)

#3#boolean operators##
# true,false

#x=int(input("enter value:"))
#if x==4:
 #   print("true")
#else:
 #print("false")

 #4#comparsion or relational ##
 # ==,!=,<,<=,>,<=

#x=int(input("enter value:"))
#if x<=4:
 #   print("x")
#else:
 #   print("exit")

 #5#logical operator##
 # and or not


# x=int(input("enter a num :"))
# if x==5 x==6:
#     print("x")
# else:
#     print("z")

#n = int(input("Enter Your Number: "))

#if n>0:
 #   print("Correct")
#else:
 #   print("You are entered wrong")


#6#membership operators##
# in,not in

#tup = (1,2,3)
#print(4  in tup)

#7#identity operators#
#is,is not

#x=10
#y=12
#print(x is y)

#################data types###########
# they are 4 types 1 number system: int,float,complex
#                  2 boolean : true,false
#                  3 sequence data types : list,tuple,dict,set
#                  4 string : "anyting",'anying'

#x=10
#print(x,type(x))

#true=non zero,non none,true,1
#false=zero, none,false,0

# crud
# create x=10,retrieve print(x), update x=20, delx

#state,behavior:behavior always depends on state. these 2 are mondatory for requirment.

#val=16
#print(val)
#val=val+2
#print(val)
#del val       ####crud#########

#list1=[1,2,3,4,5]
#print(list1)
#print(list1[1])
#list1[1] = 8
#print(list1)
#del list1
#print(list)


#################33keywords#############33
#unique reserved words that cant use as identifiers,variables,functions.keywords are used for define syntax
# and structure of programming.totally there 35 keywords.smallest unit inside the programm.ex:if,else,elif

#x=int(input('enter value:'))
#if(x==10):
 #   print(x)
#else:
 #   print("welcome")


#############decision making##########
#condition based scenarios for particular user it will work only once in that iteration after exit
#if there are only 1 or 2 options then we use this condion,based on conditions it will work
# condition : if,if else,if elif else,
#static initialisation : in prgrm itself assign the value (hardcoding) ex : x=10
#dynamic initialisation : while in running assign the value exp : enter value 10


#x= int(input("enter value:"))
#if x<=5:
#    print("valid")
#else:
 #   print("invalid")


##write a second largest number,
# x=int(input("enter value 1 "))
# y=int(input("enter value 2 "))
# z=int(input("enter value 3 "))
# if x>y and x<z or x<y and x>z:
#    print(x," second largest num ")
# elif y>x and y<z or y<x and y>z:
#    print(y,"second largest num ")
# elif z>x and z<y or z<x and z>y:
#     print(z," second largest num ")

#  write a prgrm,using any operator with 2 numbers.
# x=int(input("enter value 1 "))
# y=int(input("enter value 2 "))
# o=input("enter  operator ")
#
# if o=="+":
#     print(x+y)
# elif o=="-":
#     print(x-y)
# elif o=="*":
#     print(x*y)
#
# elif o=="/":
#     print(x/y)
#
## find the even numers between 1-10

# i = 1
# while i<=10:
#     print(i)
#     i+=2

# start=int(input("enter start num"))
# end=int(input("enter end num"))
# for num in range(start,end+1):
#     if num%2==0:
#         print(num,end=" ")

##from the given list find the even numbers
# list=[1,2,3,4,5,6,7,8]
# for list in range(4,10):
#     if list%2==0:
#         print(list)

#################################loops & controlling sttements############3
## loops :multiple statements(repeatable tasks) we use loops,iterations  of multiple data
#pass,continue,break : controlling statements
# continue: if there are multiple statements ,we want to skip particular stmnt,runs remaining we use continue after stmnt
# pass : to escape or avoid the error then we use or to dont know about further step need time means we use
# break : we want to stop itertion ,stmnt will not executed ,breaks the loop and come out of it,wont execute the prgrm
## using for loop for continue,print 10-100 numbers divisible by 5 and skip the 10 divisibles
# for x in range(10,100):
#         if x%5==0:
#             if x%10==0:
#                     continue
#
#             print(x)

## using while loop for continue,print the num 1,10 skip 5
# x=int(input("enter value :"))
# while  x<=10:
#         x+=1
#         if x==5:
#                 continue
#         print(x)

# pass : write a prgrm to enter any value for input by using pass

# x=int(input("enter value :"))
# if x<=20:
#         print("valid")
# else:
#     pass

# break :write a progrm in range of 10 with using break of 5

# x=range(1,10)
# for x in range(10):
#         if x<=10:
#              print( x )
#              x+=1
#         if x==5:
#             break
#             print("---end of the loop")


############## data types,data structure,sequence of data types,strings###########
#data types 1 numbers(int,float,complex),boolean(true,false),string(set of char enclosed  with "" and '')
# data structure : string,list,tuple,dictionary,set,frozen
# sequence of data types :6: string,list,tuple,range
# strings :indexing,slicing,adding,multiplying,checking for membership,length,max,min
# unicode : it will check the 16 bits or 2 bytes to read or allocate

#indexing
#str = "bangalore"
#print(str[1])

#lenth of list or index
#list=[1,2,3,4,5,6]
#if list[1]==1:
 #       print(list[1])
#else:
 #       print(len(list))

## write a progrm to print range of i
#for i in range(2,10):
#        print(i)
#for i in range(6,-2,-9):
 #       for j in range(i):
  #              print(j)

#msg1="bangalore"
#msg2="karnataka"
#print(msg1[0] , msg2[1]) indexing
#print(msg1+msg2) adding
#print(msg1[::])  slicing
#print(msg1*msg2) multiply

#print(msg1[1::])
# print(msg1[:1:])
# print(msg1[::1])
#print(msg1[2:7]) strt,stop : positive
#print(msg2[-6:-3]) strt,stop : negative
#print(msg2[1:8:1]) start,stop,step :positive

# write a prgrm index multiplication by given 2 lists
# list1=[1,2,3,4]
# list2=[9,8,7,6]
# print(list1[1]*list2[1])

#write a program using a string of memebership
# str1="bangalore"
# str2="mangalore"
# if str2[1]in str1:
#         print(str1)
# else:
#         print(str2[1])

#write a prgrm to find max and min in a given list
# list1=[1,2,3,4]
# list2=[9,8,7,6]
# if list1[3] is not max:
#     print(max(list1))
# else:
#     print(min(list2))

#############strings 16-6-22#######
## string : 40 functions
# list : 10 functions
# tuple : 2-3 functions
# dict : 10 functions
# set : 2 functions
# int:2 fun
# float : 2 fun
#bool : 2 function
# operations 8 types
# built in function
# algorithm
#using functions
# opps
# exception handling
# file  handling
# database interaction mvc
# ui interaction
# state : user giving input
# behavior : function/method(opps) performing task
# loops,operators,decision making


# lenth of the string ######################################################
#x="bangalore"
#print(len(x))

#x = "bangalore"
#if len(x)!=0:
#    print(len(x))
#else:
 #   print(x)

#alogorithm
# msg="bangalore"
# le=0
# for char in msg:
#     le+=1
#     print(len(msg),le)
#
# count char in string ##############################################################
#x="bangalore is"
#print(x.count('a'))

#x="mangalore to bangalore"
#count=0
#if count<=4:
 #   count+=1
  #  print(x.count('e'))

# x="chennai"
# count=0
# for i in x:
#     if i=='a':
#         count=count+1
#         print(x.count('a'))

##string slicing

# str1="bangalore"
# print(str1[::2])

#algorithm
#1#str1="bangalore"
#for char in str1:
 #   print(str1[0:8:2])
#2# str1="bangalore"
# while str1[6]=='o':
#     print(str1[0:9])

###lenth of the longest string in python

#str1="python"
#print(max(str1))  # output=y

#str1=input("Enter Your Name: ")
# str2=input("Enter Your Name: ")
# str3=input("Enter Your Name: ")
#
# a = len(str1)
# b = len(str2)
# c = len(str3)
#
#
# if a>b and a>c:
#     print(a,"is largest number")
# elif a==b:
#     print("a and b are largest number")
# elif a==c:
#     print("a and c are largest numbers")
# elif b==c:
#     print("b and c are largest numbers")
# elif b>c and b<c:
#     print(b,"is the largest number")
# else:
#     print(c,"is the largest number")


## swap the first and last char in a string
# str1="python"
# a=str1[0]#p
# b=str1[5]#n
# a,b=b,a#(p,n=n,p)
# c=a+str1[1:5]+b
# print(c)

#x="bangalore"
#print(x.swapcase())

# x="bangalore"
# a=x[0]#b
# b=x[8]#e
# c=b+x[1:7]+a#e+angalor+b
# print(c)

# write a prgrm to reverse of a num
# x=int(input("enter a number :"))
# rev=0
# while x!=0:
#     rev=rev*10+x%10
#     x = x//10
# print(rev)
 
## remove odd index values
# x="apple"
# x[0]==a
# print(del)
#del+=1

# length of a string
# x="bangalore"
# print(len(x))

#algorithm
# x=str(input("enter value :"))
# length_of_x=0
# for i in x:
#     length_of_x+=1
# print(length_of_x)

#count of string

#x="bangalore"
#print(x.count('a'))

# algorithm
# x=str(input("enter names"))
# total=0
# for i in range(len(x)):
#     total+=1
# print("count of char in str", total)

#string slicing

# x="bangalore"
# print(x[::1])

# algorithm
# x="bangalore"
# y=0
# for i in x:
#     y+=1
# print(x[0:8:2])

#length of logest string in python

# x=["mango","banana","guava","oranges"]
# y=0
# for i in max(x):
#     y+=1
# print(max(x))

#first and last char swapping

# str = str(input("Enter Your Name: "))
# new_str = str[-1:] + str[1:-1] +str[:1]
# print(new_str)

#remove odd index values
# a="bangalore"
# b=""
# for i in range(0,len(a)):
#     if (i%2==0):
#         b=b+a[i]
# print("original a :",a)
# print("final value of b :",b)

#count words in string

# x="kalyan going to office"
# count_of_words=len(x.split())
# print(count_of_words,x)

#algorithm
# x="kalayn is going to office"
# count_of_words=1
# i=0
# while(i<len(x)):
#     if (x[i]==" " or x=="/n" or x=="/t"):
#         count_of_words+=1
#     i+=1
# print("total number of words in a string=",count_of_words)


#list
# sum of elements
# x=[1,2,3,4,5,6,7,8]
# tot=0
# for i in range(0,len(x)):
#     tot+=x[i]
# print("sum of elements=",tot )

# multiply of elements
# x=[1,2,3]
# tot=1
# for i in range(0,len(x)):
#     tot*=x[i]
# print("multiply of x=",tot)

#largest number from the list
# x=[1,2,5,7,8]
# print(max(x))

#algorithm
# x=[3,6,8]
# for i in range(0,len(x)):
# print(max(x))

#remove duplicates
# x=[1,1,2,2,4,6,4,6]
# y=[]
# for i in x:
#     if i not in y:
#      y.append(i)
# print(y)

#check list is emty or not
# x=[1,2,3]
# if len(x)==0:
#  print("List is Empty")
#
# else:
#  print("List is not empty")


#clone or copy
# x=[1,2,3,4]
# print(x.copy())

  #shuffle list and print
# import random
# list=[1,2,3,4]
# random.shuffle(list)
# print(list)

#convert a string to a list
# x="bangalore"
# y=list(x)
# print(print(y))
# print(type(y))

#remove duplicates from list of list
# x=[[1,2],[2,3],[1,2]]
# y=[]
# for i in x:
#     if i not in y:
#      y.append(i)
# print(y)

# dictionary
#Prints each item and its corresponding type from the following list.
# data={'name':'raji','id':'012','role':'engineer'}
# print(data['name'],type ('name'))
# print(data['id'],type('id'))
# print(data['role'],type('role'))

# algorithm
# dict={1:'raji',2:'kalyan',3:'sai',4:'kumar'}
# for key,val in dict.items():
#     print(key,"-----",val,type(dict))

##To sort (ascending and descending) a dictionary by value

# dict={1:'raji',2:'kalyan',3:'sai',4:'kumar'}
# items=dict.items()
# print(sort(items))


# dict1 = {1:345, 2:654}
# dict2 = dict1.copy()
# print("-----Before modification-----------")
# print("Dict1 copy : ", dict1)
# print("Dict2 copy : ", dict2)
# print("-----After modification-----------")
# dict2['name'] = 'raji'
# print("Dict1 copy : ", dict1)
# print("Dict2 copy : ", dict2)



