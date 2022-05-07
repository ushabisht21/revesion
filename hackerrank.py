# num=int(input())
# k=[]
# for i in range(num):
#     sum=int(input())
#     k.append(sum)
# print(k)



# import math
# ab=int(input())
# bc=int(input())
# tita=(math.atan(ab/bc))
# tita_to_degree=round(math.degrees(tita))
# print(tita_to_degree,chr(176),sep=' ')


# a=int(input())
# m=int(input())
# rs=int(input())
# if a>m:
#     k=a-m
#     l=rs-k
#     print(l)
# if m>a:
#     k1=m-a
#     s=rs-k
# print(s)



# from math import atan ,degrees
# ab=int(input())
# bc=int(input())
 
# theta=round(degrees(atan(ab/bc)))
# print(theta,chr(176),sep=' ')


# T=int(input())
# for _ in range(T):
#     C,D,L=map(int,input().split())
#     total = (C+D)*4
#     min_no=C-D*2
#     if(total>=L and L%4==0 and (D+min_no)*4<=L):
#         print("yes")
#     else:
#         print("no")


# t=int(input())
# for i in range(t):
#      c,d,l=map(int,input().split())
#      total=(c+d)*4
#      if(c>(d*2)):
#         min_legs=(c-(d*2)+d)*4
#      else:
#         min_legs=(d*4)
#      if l%4==0 and l>=min_legs and l<=total:
#          print("yes")
#      else:
#           print("no")




# t = int(input("how much time code will run :"))
# while(t>0):
#     cats, dogs, legs = map(int, input(" :-").split())
#     max_legs = (dogs + cats) * 4
 
#     if((2 * dogs) >= cats):
#         min_legs = 4 * dogs

#     else:
#         min_legs = (cats - (2*dogs)) * 4 + dogs * 4

#     if(legs < min_legs or legs > max_legs):
#         print("no")

#     else:
#         if(legs % 4 == 0):
#             print("yes")
#         else:
#             print("no")
#     t -= 1