#Problem 1
#Code

from abc import *   
class Book(metaclass=ABCMeta):
    @abstractmethod
    def get_rental_price(self, day):
        pass
    
    
class ComicBook(Book):
    def get_rental_price(self, day):
        cost = 500
        day -= 2
        if day > 0:
            cost += 200*day
        return cost
    
    
class Novel(Book):
    def get_rental_price(self, day):
        cost = 1000
        day -= 3
        if day > 0:
            cost += 300
        return cost
    
    
def solution1(book_types, day):
    books = []
    for types in book_types:
        if types == "comic":
            books.append(ComicBook())
        elif types == "novel":
            books.append(Novel())
    total_price = 0
    for book in books:
        total_price += book.get_rental_price(day)
    return total_price


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
book_types = ["comic", "comic", "novel"]
day = 4
ret = solution1(book_types, day)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#Problem 2
#Code

def func_a2(times):
    hour = int(times[:2])
    minute = int(times[3:])
    return hour*60 + minute

def solution2(subway_times, current_time):
    current_minute = func_a2(current_time)
    INF = 1000000000
    answer = INF
    for s in subway_times:
        subway_minute = func_a2(s)
        if subway_minute >= current_minute:
            answer = subway_minute - current_minute
            break
    if answer == INF:
        return -1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.

subway_times1 = ["05:31", "11:59", "13:30", "23:32"]
current_time1 = "12:00"
ret1 = solution2(subway_times1, current_time1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

subway_times2 = ["14:31", "15:31"]
current_time2 = "15:31"
ret2 = solution2(subway_times2, current_time2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

#Problem 3
#Code

def func_a3(n):
    ret = 1
    while n > 0:
        ret *= 10
        n -= 1
    return ret

def func_b3(n):
    ret = 0
    while n > 0:
        ret += 1
        n //= 10
    return ret

def func_c3(n):
    ret = 0
    while n > 0:
        ret += n%10
        n //= 10
    return ret

def solution3(num):
    next_num = num
    while True:
        next_num += 1
        length = func_b3(next_num)
        if length % 2:
            continue
        
        divisor = func_a3(length//2)  
        front = next_num // divisor
        back = next_num % divisor
        
        front_sum = func_c3(front)
        back_sum = func_c3(back)
        if front_sum == back_sum:
            break
            
    return next_num - num

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
num1_3 = 1
ret1_3 = solution3(num1_3)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1_3, "입니다.")

num2_3 = 235386
ret2_3 = solution3(num2_3)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2_3, "입니다.")

#Problem 4
#Code

import math
def solution4(arr, K):
    length = len(arr)
    count = 0
    for i in range(length):
        for j in range(i+1,length):
            for f in range(j+1,length):
                num = i + j + f
                if num%K == 0:
                    count += 1
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 2, 3, 4, 5]
K = 3
ret_4 = solution4(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret_4, " 입니다.")

#Problem 5
#Code

def solution5(arr):
    count = 0
    up = [1 for _ in range(len(arr))]
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            up[i] = up[i-1]+1
        
    answer = max(up)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret_5 = solution5(arr)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret_5, "입니다.")
