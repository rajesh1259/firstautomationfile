from random import shuffle
# class one:
#     def methodone(self):
#         print("this method first")
#
#
#     def methodonepart(self):
#         print("method's part")
#
#     def localfile(self):
#         print("local file is added")


# a=input("enter first no : ")
# a=int(a)
# b=input("enter second no: ")
# b=int(b)
# c=input("enter the third no: ")
# c=int(c)
#
#find largest no

# if(a>b and a>c):
#     print("a islargest number")
# elif(b>a and b >c):
#     print("b islargest number")
# elif(c>a and c>b):
#     print("c islargest number")

#smallest number

# enlgish=int(input("enter marks"))
# math=int(input("enter marks"))
# physics=int(input("enter marks"))
# chemestry=int(input("enter marks"))
# biology=int(input("enter marks"))
# avg=(enlgish+math+physics+chemestry+biology)/5
# if(avg>90):
#     print("grade A")
# elif(avg>80):
#     print("grade B")
# elif(avg>70):
#     print("grade c")
# elif(avg>60):
#     print("grade D")
# elif(avg>50):
#     print("grade E")
# elif(avg>40):
#     print("grade F")
# else:
#     print("low grade")

# num=int(input("enter any number : "))
# for i in range(1,11):
#     if (i==5):
#         continue
#     print(num*i)

#a=int(input("enter first value"))
#b=int(input("enter second value"))
# c=0
# c=a
# a=b
# b=c
#
# print(a)
# print(b)

#inrasing traingle pattern

#for i in range(5):
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# decreasing traingle pattern
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# right sided  traingle
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# #right sided taingle
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()


# hill pattern
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# reverse hill pattern
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()


# def mult(a,b):
#     return a*b
# def addn(te22,c):
#     return te22+c
# te22=mult(2,4)
# te11=addn(te22,10)
# print(te22,te11)
#
# numbers=[24,56,2,88,55]
# def find_largest(numbers):
#     largest=numbers[0]
#     for i in numbers:
#         if i > largest:
#             largest=i
#     return largest
#
#
# data=find_largest(numbers)
# print(data)


# # the_list=["akash","ramr","vijayv"]
# count=0
#
# for i in the_list:
#
#     '''if (len(i)>=2 and i[0]==i[-1]):
#         count=count+1
# print(count)'''


# the_list=[2,4,5,2,6,6,5,4]
# new_list=[]
# for i in the_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# the_list=[]
# if not the_list:
#     print("list is empty")
# else:
#     for i in the_list:
#         print(i,end=" ")

# the_list=[2,4,5,2,6,6,5,4]
# new_list=list(the_list)
#
# print(new_list)
# print(the_list)


# the_list=["akash","ab","cd","ramr","vijayv"]
# n=1
# for i in the_list:
#     if len(i)>n:
#         print(i)

# list1=[1,2,4,5,6]
# list2=[2,4,6,8]
# for i in list1:
#     for j in list2:
#         if i==j:
#             print("True")
#         break


# def myfun(list1,list2):
#     for i in list1:
#         if i in list2:
#             return True
#         else:
#             return False
#
#
#
# list1=[1,2,5,4]
# list2=[4,6,8]
# print(myfun(list1,list2))

# list5=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# del list5[0]
# print(list5)

# test=[1,2,3,4,5,6,7,8,9,10]
# #new_test=[i for i in test if i%2!=0]
# shuffle(test)
# print(test)


# listd=[]
#
# for i in range(1,21):
#     listd.append(i**2)
# #print(listd[:6])
# print(listd[6:])

# list1 = [1, 3, 10,5, 7,8, 9]
# list2=[4,5,6,3,2,11]
# l3=list(set(list1)-set(list2))
# l4=list(set(list2)-set(list1))
#
# print(l3)
# print(l4)
# print(l3+l4)

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={}
# for i in (dic1,dic2,dic3):
#     dic4.update(i)
# print(dic4)
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# if 20 in d:
#     print("present")
# else:
#     print("not present")

# for i in d.keys():
#     print(d.keys(i))
# #     if i==d[2]:
# #         print("present")
# #     else:
# #         print("not present")

# d = {'x': 10, 'y': 20, 'z': 30}
# for i,j in d.items():
# #     print(i,j)
#
# jclass Employee:
#     leaves=10
#     def myfun(self,a,b):
#         c=a+b
#         print(c)
#     @classmethod
#     def test(cls):
#         cls.leaves
#
#
#
# data=Employee()
# print(data.test)

# class Text:
#     no_leaves=10
#
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#
#     def mymethod(self):
#         print(self.a+self.b)
#
#     @classmethod
#     def my_newmethod(cls,no_leaves):
#         cls.no_leaves=no_leaves
#
# data=Text(2,4)
# data.my_newmethod(24)
# print(data.no_leaves)


# arr = [3, 8, 1, 5, 9, 2, 7]
# print(arr)
#

# # initialize max_num and min_num to the first element in the array
# max_num = arr[0]
# min_num = arr[0]
#
# # iterate through the array and update max_num and min_num as necessary
# for num in arr:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num
#
# print("Maximum element is:", max_num)
# print("Minimum element is:", min_num)

# def myfub(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     elif n<=0:
#         print("doest exist")
#     else:
#         print(a)
#         print(b)
#
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
#
#
#
# myfub(-1)
#
# the_list=[2,5,3,7,8,44,22,4]
# min_num=the_list[0]
# max_num=the_list[0]
# for i in the_list:
#     if i>max_num:
#         max_num=i
#     elif i<min_num:
#         min_num=i
# print(max_num,min_num)

# the_list=[2,5,3,7,8,44,22,4]
# count=0
# for i in the_list:
#     count=count+1
# print(count)

# the_list=[2,5,3,7,8,44,22,4]
# temp=the_list[0]
# n=len(the_list)
# the_list[0]=the_list[n-1]
# the_list[n-1]=temp
# print(the_list)

# the_list=[2,5,3,7,8,44,22,4]
# first=the_list[0]
# last=the_list[-1]
# the_list[0]=last
# the_list[-1]=first
# print(the_list)
# the_list=[2,5,3,7,8,44,22,4]
# num=4
# flag=0
# for i in the_list:
#     if i==num:
#         print("elment found")
#         flag=1
#         break
# if flag==0:
#     print("not found")


# the_list=[2,5,3,7,8,44,22,4]
# new_list=[]
# new_list.extend(the_list)
# print(new_list)
#
# the_list=[2,5,3,7,8,44,22,4,8,22,8,45,8]
# num=int(input("enter any number "))
# count=0
# for i in the_list:
#     if i==num:
#         count=count+1
# print(count)

# the_list=[2,5,3,7,8,44,22,4,8,22,8,45,8]
# sum=0
# for i in the_list:
#     sum=sum+i
# print(sum)

# the_list=[2,5,3,7,8,44,22,4,8,22,8,45,8]
# num=the_list[0]
# for i in the_list:
#     if i > num:
#         num=i
# print(num)

# def reverse_words(string):
#     words = string.split()
#     reversed_words = words[::-1]
#     reversed_string = " ".join(reversed_words)
#     return reversed_string
#
# # Example usage:
# string = "Hello world! How are you?"
# reversed_string = reverse_words(string)
# print(reversed_string)

# string = "Hello world! How are you?"
# data=string.split(" ")
# revers_word=data[::-1]
# print(revers_word)
# revese_string= " ".join(revers_word)
# print(revese_string)

# string = "Hello world! How are you?"
# new_string=string.split(" ")
# print(new_string)
# new_fin=new_string[::-1]
# fin_data=" ".join(new_fin)
# print(fin_data)

# s_string="Welcome to python programming"
# if "pythonrr" in s_string:
#     print("present")
# else:
#     print("not present")

# num=int(input("enter any num"))
# for i in range(1,11):
#     print(i*num)


# def myfun(str1,str2):
#     if len(str1) > 0 and len(str2) > 0:
#         print(str1[0] + str2[-1])
#     elif len(str1) <= 0 and len(str2) > 0:
#         print("@" + str2[-1])
#     elif len(str1) > 0 and len(str2) <= 0:
#         print(str1[0] + "@")
#     else:
#         print("@@")
#
# myfun("","")

# def myfun(str1):
#     if str1.index("bad")==0 or str1.index("bad")==1:
#         return True
#     else:
#         return False
# print(myfun("ddsf"))
#
# stringss="The"
# for i in stringss:
#     print(i*2,end="")

# stringss="aaacdebbb"
# print(stringss.count("code"))

# def myfun(n):
#     if n==1:
#         return list(range(0,1))
#     else:
#         return list(range(0,n,1))
# print(myfun(5))

# the_list=[1,4,5,7,66]
# max_num=the_list[0]
# min_num=the_list[0]
# for i in the_list:
#     if i > max_num:
#         max_num=i
#     elif i < min_num:
#         min_num=i
# print(max_num)
# print(min_num)
# print(max_num-min_num)

# def only_ones_and_fours(arr):
#     for num in arr:
#         if num != 1 and num != 4:
#             return False
#     return True
#
# my_arr = [1, 4, 1, 4, 4, 1]
# print(only_ones_and_fours(my_arr)) # Output: True

# str1=input("enter any string ")
# char=input("enter any character")
# count=0
# for i in str1:
#     if i==char:
#         count=count+1
# print(count)


# str1="listen"
# str2="silentf"
# if sorted(str1)==sorted(str2):
#     print("anagram")
# else:
#     print("not an anagram")


# def is_anagram(str1, str2):
#     # Remove spaces and convert to lowercase
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
#
#     # Check if sorted versions of strings are equal
#     return sorted(str1) == sorted(str2)
#
#
#
# # Test case 1
# str1 = "listen"
# str2 = "silent"
# print(is_anagram(str1, str2))  # Output: True

# ch=input("enter any character ")
# if (ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
#     print("vovel")
# else:
#     print("not a vovel")

num = int(input("Enter an integer: "))
reverse = 0

while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print("The reverse of the integer is:", reverse)