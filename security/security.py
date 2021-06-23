# Caesar 암호
# arr1 =["A","B","C","D","E","F","G","H","I","J,","K","L","M","N","O","P","Q","R","S","T","U","W","X","Y","Z"]
# # vale = ["C","D","F"]
# vale = input("암호입력 : ")
# vale = list(vale)
# key=int(input("키를 입력 : "))
# for i in vale:
#     arr1_vale = arr1.index(i) +key
#     print(arr1[arr1_vale % len(arr1)])

# RSA 암호
from random import *
# 소수 확인 함수
def number(num):
    if num != 1:
        for f in range(2,num):
            if num % f ==0:
                return False
    else:
        return False
    return True
# 최대 공약수 추출
def gcd(a,b):
    temp=0
    while True:
        if a< b:
            temp =a
            a = b
            b = temp
        if a%b ==0:
            return b
        else:
            temp =a%b
            a=b
            b=temp
# 메인
def main():
    p =0
    q =0
    while True:
        num = randint(1,101)
        num2 = randint(1,101)
        if number(num) and number(num2):
            p = num
            q =num2
            break
    print(p,q)
    N =p*q
    P=(p-1)*(q-1)
    arr =[]
    for i in range(1,P+1):
        a =gcd(P,i)
        if a == 1:
            arr.append(i)
    d=0 #개인키
    e =arr[1] #공개키
    for i in range(P):
        if i * e % P == 1:
            d =i
    print("공개키는",N,e)
    print("개인키는",N,d)
    # print(arr)

    M = int(input("암호화 메세지 : "))
    c = M**e%N  #암호화

    m = c**d%N  #복호화

    print(c)
    print(m)

main()