'''list'''

# ls=[1,2,3,4,5,6]
# # print (ls)
# ls.append()




'''tuple'''

# # tp=(1,2,3,4,5,6,7"eight")

# tp=tuple((1,2,3,4,5))

# print(tp)

'''set'''

# s1={1,2,3,4,"hello",6,7,8}

# s2={2,3,44,56,666}

# s3=s1.intersection(s2)
# print(s3)

'''dictionary'''


# dict={'name':'alice','age':20}

# # print (dict['name'])
# a=dict.keys()



'''for loop'''

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("\n")
    
    
# for i in range(1,6):
#      for j in range(1,i+1):
#       print(i,end="")
#      print("\n")
     
# n=5     
# for i in range(n):
#    for j in range(i + 1):
#       print("*",end="")
# print("\n")

    
    
# ls=[]
# for i in range(1,101):
#     for j in 
#      ls.append(i)
# print(ls)

# ls=[]
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         ls.append("fizzbuzz") 
#     elif i%5==0:
#         ls.append("buzz")
#     elif i%3==0:
#         ls.append("fizz")
#     else:
#         print(ls)
    
'''for questions'''

'''1'''
# n=6
# for i in range(n):
#     for j in range(i + 1):
#         print("*",end="")
#     print("\n")
    
# for i in range(n -1,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print("\n")

'''2'''




'''3'''
# numbers=(1,2,3,4,5,6,7,8,9)
# even_count = 0
# odd_count= 0

# for i in numbers:
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#     print("number of even number:",even_count)
#     print("number of odd numbers:",odd_count)
    


'''6'''

# n= 5
# for i in range(1,n+ 1):
    
'''listlicing'''    
# ls=[28,56,34,66,78,90,96]
# print(ls[])   
    
'''listco'''

# ls1=[10,20,30,40,50,60,70]

# ls2=[i**2 for i in range(1,11) if i<80]

# print(ls2)


'''string'''

# s="    midhun midhu    "

# print(len(s))
# print(s.upper())
# print(s.lower(1))
# print(s.strip())
# print(s.replace("midhun","midhu"))

# s="apple,orange,graps,mango,apple"

# a=s.split("-")

'''funtions'''

# def demo():
#     a=10
#     b=20
#     print(a+b)
    
# demo()


# def demo():
#     print("===========")
#     print("------------")
    
# demo()
# print("hi")
# demo()

# def add(a,b):
#     print(a+b)
    
    
    
# num1=int(input("enter a value :"))
# num2=int(input("enter a value :"))


# add(num1,num2)
# num1=int(input("enter a value :"))


'''break and continue'''

# for i in range(1,21):
    
#      print(i)
#      if i==11:       
#                 break
            
            
# for i in range(1,21):
    
#     print(i)
#     if i==12:
#         continue


# def m(n):
#    for i in range(1,11):
#        a=i*n
#        print(i,"*=",a)
# n=int(input("enter a value:"))



# def add(a,b):   
#     return a+b

# x=add(5,5)
# print(x)

'''function questions'''

# def add(a,b):
#     return a+b
# n=int(input("enter a value :"))
# length1=4
# width1=4
# x=add(length1,width1)
# print(x)




# def asd():
#     a=10
#     print(a)
# asd()


# a=10
# def asd():
#     print("inside asd()",a)
# asd()
# print("outside asd()",a)


# def asd():
#     a=10
#     def bsd():
#         print("inside asd()",a)
#     bsd()
# asd()


# a=1
# def asd(b):
#     b=b+1
#     if b<=10:
#         print(b)
#         asd(b)
# asd(a)



# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# res=fact(1)
# print(res)



# def rec(n):
#     if n>0:
#         print(n)
#         rec(n-1)
# rec(200)


# i=1
# while True:
#     print (i)
#     i=i+1
#     if i==11:
#         break    




# ls=[]
# while True:
     
#   print("-------------------------------")
#   print("1-add todo ")
#   print("2-display todo ")
#   print("3-delete todo ")
#   print("4-exit")
#   print("-------------------------------")

#   a=input("enter your choice :")
#   if a==1:
#    b=(input("enter todo :"))
#    ls.append(b)


#   elif a==2: 
#     print("")
    
#   elif a==3:
#     c=(input("enter to delete :"))
#     ls.remove(c)
    
#   elif a==4:
#     print("thank you")
#     break
          
#   else:
#     print("***invalid input***")
    


'''OOPS'''



'''single inheritence'''

# class vehicle:
#     color="red"
#     def engine(self):
#         print("all vehicles have engine")  
# class car(vehicle):
#     def fourwheel(self):
#         print("car have 4 wheel",self.color)
# c=car()
# c.fourwheel()
# c.engine()


'''multi level inheritence'''


# class granpa:
#     def kashandi(self):
#         print("kashandi family")
#     def farmer(self):
#         print("farmer")
# class father(granpa):
#     def driver(self):
#         print("driver")
#     def reader(self):
#         print("reader")
# class me(father):
#     def swimming(self):
#         print("swimming")
#     def engineer(self):
#         print("engineer")
# class child(me):
#     def gamer(self):
#         print("gemer")
# ob= child()
# ob.




# class A:
#     _a=10
#     def _disp(self):
#         print(self._a)
# obj=A()
# obj._disp()
# print(obj._a)



# from abc import ABC,abstractmethod
# class vehicle(ABC):
#     def engine(self):
#         print("engine provide")
#     @abstractmethod
#     def gear(self):
#         pass
# class car(vehicle):
#     def gear(self):
#         print("automatic gear")
# class truck(vehicle):
#     def wheel(self):
#         print("heavy")
#     def gear(self):
#         print("manuel gear")
# c=car()
# c.gear()
# t=truck()
# t.gear()