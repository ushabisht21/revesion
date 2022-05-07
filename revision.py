# from itertools import count



# num=int(input("enter the number"))
# i=1
# count=0
# while i<=num:
#     if num%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print("it is prime number")
# else:
#     print("it is not prime number")



# for num in range (1,200):
#     if all(num%i!=0 for i in range(2,num)):
#         print(num,"it is praim")



# a=[1,2,3,4,5,7,8,9]
# k=[]
# i=0
# while a:
#     min=a[i]
#     for x in a:
#         min=x
#     k.append(min)
#     a.remove(min)
# print(k)



# a=[1,2,3,4,5,7,8,9]
# a.reverse()
# print(a)



# a="i am usha"
# print(len(a.split()))
# print(len(a))



# l=[20,30,40,50,50,20]
# k=[]
# for i in l:
#     if l.count(i)>1 and i not in k:
#         k.append(i)
# print(k)



# l=[20,30,40,50,50,20]
# k=[]
# i=0
# while i<len(l):
#     if l[i] not in k:
#         k.append(l[i])
#     i=i+1
# print(k)


# a=["23","usha","36",89,"8"]
# i=0
# k=[]
# while i<len(a):
#     if type (a[i])==str:
#         k.append(a[i])
#     i=i+1
# print(k)







# a=[1,0,5,3,0,0,7,8,0]
# # =[1,5,3,7,8,0,0,0,0]
# i=0
# k=[]
# s=[]
# while i<len(a):
#     if a[i]==0:
#         k.append(a[i])
#     if a[i]!=0:
#         s.append(a[i])
#     i=i+1
# print(s+k)





# size=int(input("enter the size"))
# a=[]
# for i in range(size):
#     val=int(input("enter the number"))
#     a.append(val)
# for i in range(size):
#     for j in range(0,size-1-1):
#         if a[j]>a[j+1]:
#             t=a[j]
#             a[j]=a[j+1]
#             a[j+1]=t
# print("sortend list is")
# print(a)


#sum of nested



# li=[4,5,6],[5,6,8],[9,10,11]
# i=0
# sum=0
# while i<len(li):
#     if i==0:
#         for j in li[i]:
#             sum+=j
#     elif i!=0:
#         s=len(li[i])
#         sum+=(li[i][s-1])
#     i=i+1
# print(sum)





# x=lambda a:a+10
# print(x(5))



# a=[10,50,60,80,90,5,45,65]
# def marks(n):
#     if n>60:
#         return True
# k=filter(marks,a)
# for i in k:
#     print(i)



# num=["2","33","5"]
# k=[]
# for i in range(len(num)):
#     num[i]=int(num[i])
#     k.append(num[i])
# print(k)



# a=["2","34","usha","56"]
# k=[]
# s=[]
# for i in range(len(a)):
#     k.append(int(a[i]))
#     s.append(str(a[i]))
#     # print(a[i])
#     print(k)
#     print()

# num=[2,3,4,5,6,7,8,9]
# square=list(map(lambda x:x*x*x,num))
# print(square)




# list=[2,3,4]
# num=reduse(lambda x,y:x*y,list)
# print(num)

# a="usha"
# b="geeta"
# b=a.join(b)
# print(b)




# a=[2,3,4,3,4,5,5,2]
# i=0
# k=[]
# count=0
# while i<len(a):
#     if a[i] not in k:
#         k.append(a[i])
#         count=count+1
#     i=i+1
# print(k,count)



# a=[10,20,10,30,40,50,40]
# d=[]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j] and a[i] not in d:
#             d.append(a[i])
# print(d)


# def common_letters():
#     str1=input("enter the name")
#     str2=input("enter the name")
#     s1=set(str1)
#     s2=set(str2)
#     lst=s1 or s2
#     print(lst)
# common_letters()



# a={23,40,10,90,40}
# print(a)
# print(type(a))


# def num(a):
#     sum=0
#     i=0
#     while i<len(a):
#         sum=sum+a[i]
#         i=i+1
#     print(sum)
# num([2,3,4,5,6])
# num([2,3])


# list_1 = [ 3, 5, 7, 3, 9, 3 ]   
# print(list_1)  
# list_1.remove(3)   
# print("After removal: ", list_1)
# ist_1 = [ 3, 5, 7, 3, 9, 3 ]   
# print(list_1)  
# del list_1[2]  
# print("After deleting: ", list_1)  


# a=[1,2,3,4,5,6,7,8]
# print(a[2:3])



# a=[1,0,2,0,3]
# i=0
# k=[]
# j=[]
# while i<len(a):
#     if a[i]==0:
#         k.append(a[i])
#     if a[i]!=0:
#         j.append(a[i])
#     i=i+1
# print(j+k)



# n=int(input("enter the number"))
# c=0
# if n>=0 and n<=12:
#     for i in range(1,7):
#         for j in range(1,7):
#             if i+j==n:
#                 c=c+1
#     print(c)
# else:
#     print(0)



# str1=input("enter the str")
# output=""
# for chr in str1:
#     if chr .isalpha():
#         var=chr
#     else:
#         num=int(chr)
#         output=output+(var*num)
# print(output)








# k=int(input("enter the range"))
# name=[]
# sir_name=[]
# age=[]
# s=[]
# for i in range(k):
#     naam=input("enter the naam")
#     name.append(naam)
#     sir_name1=input("enter the sir_name")
#     sir_name.append(sir_name1)
#     age1=int(input("enter the age"))
#     age.append(age1)
# print(name)
# print(age)
# print(sir_name)
# print(name,sir_name,age)


# t=int(input())
# for i in range(t):
#       x,m,d=map(int(input().split()))
#       if (x*m)>(x+d):
#             print(x*m)
#       else:
#             print(x+m)




# a=[10,20,39,48,34,5,6]
# val=list(filter(lambda a:a%2==0,a))
# squ=list(map(lambda a:a*a,val))
# print(val) 
# print(squ)



# def my_function(a):
#       if a%2==0:
#             return True
#       else:
#             return False
# def sew(a):
#       return a*a
# val=list(filter(my_function,a))
# print(val)




# a=[12,34,90,50,78,45]
# a.sort()
# print(a)
# print(a[1])





#       dic=[]
#       name=input()
#       score=float(input())
#       if score in dic:
#             dic[score].append(name)
#       else:
#             dic[score]=name
# print(dic)
