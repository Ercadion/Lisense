#Problem 1
#Code
from abc import *
class DeliveryStore(metaclass=ABCMeta):
    @abstractmethod
    def set_order_list(self, order_list):
        pass
    
    @abstractmethod
    def get_total_price(self):
        pass
    
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class PizzaStore(DeliveryStore):
    def __init__(self):
        menu_names = ["Cheese", "Potato", "Shrimp", "Pineapple", "Meatball"]
        menu_prices = [11100, 12600, 13300, 21000, 19500];
        self.menu_list = []
        for i in range(5):
            self.menu_list.append(Food(menu_names[i], menu_prices[i]))
        
        self.order_list = []
    
    def set_order_list(self, order_list):
        for order in order_list:
            self.order_list.append(order)

    def get_total_price(self):
        total_price = 0
        for order in self.order_list:
            for menu in self.menu_list:
                if order == menu.name:
                    total_price += menu.price
        return total_price 
            
def solution(order_list):
    delivery_store = PizzaStore()
    
    delivery_store.set_order_list(order_list)
    total_price = delivery_store.get_total_price()
    return total_price

#The following is code to output testcase.
order_list = ["Cheese", "Pineapple", "Meatball"]
ret = solution(order_list)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")

#Problem 2
#Code
def func_a2(string, length):
    padZero = ""
    padSize = length - len(string)
    for i in range(padSize):
        padZero += "0"
    return padZero + string

def solution2(binaryA, binaryB):
    max_length = max(len(binaryA), len(binaryB))
    binaryA = func_a2(binaryA, max_length)
    binaryB = func_a2(binaryB, max_length)
    
    hamming_distance = 0
    for i in range(max_length):
        if binaryA[i]!=binaryB[i]:
            hamming_distance += 1
    return hamming_distance

#The following is code to output testcase.
binaryA = "10010"
binaryB = "110"
ret = solution2(binaryA, binaryB)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")

#Problem 3
#Code
def func_a3(numA, numB, exp):
    if exp == '+':
        return numA + numB
    elif exp == '-':
        return numA - numB
    elif exp == '*':
        return numA * numB
    
def func_b3(exp):
    for index, value in enumerate(exp):
        if value == '+' or value == '-' or value == '*':
            return index
        
def func_c3(exp, idx):
    numA = int(exp[:idx])
    numB = int(exp[idx + 1:])
    return numA, numB

def solution3(expression):
    exp_index = func_b3(expression)
    first_num, second_num = func_c3(expression, exp_index)
    result = func_a3(first_num, second_num, expression[exp_index])
    return result

#The following is code to output testcase.
expression = "123+12"
ret = solution3(expression)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")

#Problem 4
#Code

import math
def solution4(num):
    num += 1
    digit =1
    while num //digit % 10 == 0:
        num += digit
        digit *= 10
    return num


#The following is code to output testcase.
num = 9949999;
ret = solution4(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")


#Problem 5
#Code

def solution5(n):
    start = 0
    length = n
    digit = 0
    if n%2 == 0:
        start += n*2
        n -=2
        while n>0:
            digit += 4*(n+1)*2
            start += 2*n
            n -= 2
        answer = digit + start
    if n%2 == 1:
        start += n*2
        n -= 2
        while n>1:
            digit += 4*(n+1)*2
            start += 2*n
            n -= 2
        answer = digit + start + length*length
    return answer


#The following is code to output testcase.
n1 = 3
ret1 = solution5(n1)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret1, ".")
    
n2 = 2
ret2 = solution5(n2)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret2, ".")

#Problem 6
#Code

def solution6(pos):
    eng = ['A','B','C','D','E','F','G','H']
    num = ['1','2','3','4','5','6','7','8']
    move_x = [1,-1,1,-1,2,-2,2,-2]
    move_y = [2,2,-2,-2,1,1,-1,-1]
    answer = 0
    eng_index = eng.index(pos[0])
    num_index = num.index(pos[1])
    for i in range(8):
        ax = (num_index + 1) + move_x[i-1]
        ay = (eng_index + 1) + move_y[i-1]
        if ax>0 and ax<=8 and ay>0 and ay<=8:
            answer += 1
    return answer

#The following is code to output testcase.
pos = "A7"
ret = solution6(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")


#Problem 7
#Code
def solution7(arrA, arrB):
    arrA_idx = 0
    arrB_idx = 0
    arrA_len = len(arrA)
    arrB_len = len(arrB)
    answer = []
    while arrB_idx <= arrB_len -1 and arrA_idx <= arrA_len:
        if arrA[arrA_idx] < arrB[arrB_idx]:
            answer.append(arrA[arrA_idx])
            arrA_idx += 1
        else:
            answer.append(arrB[arrB_idx])
            arrB_idx += 1
    while arrA_idx < arrA_len:
        answer.append(arrA[arrA_idx])
        arrA_idx += 1
    while arrB_idx < arrB_len:
        answer.append(arrB[arrB_idx])
        arrB_idx += 1
    return answer


#The following is code to output testcase.
arrA = [-2, 3, 5, 9]
arrB = [0, 1, 5]
ret = solution7(arrA, arrB);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")

#Problem 8
#Code

def solution8(N, votes):
    vote_counter = [0 for i in range(N+1)]
    for i in votes:
        vote_counter[i] += 1
        
    max_val = max(vote_counter)

    answer = []
    for idx in range(1, N + 1):
        if vote_counter[idx] == max_val:
            answer.append(idx)
    return answer


#The following is code to output testcase. The code below is correct and you shall correct solution function.
N1 = 5
votes1 = [1,5,4,3,2,5,2,5,5,4]
ret1 = solution8(N1, votes1)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret1, " .")


N2 = 4
votes2 = [1, 3, 2, 3, 2]
ret2 = solution8(N2, votes2)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret2, " .")

#Problem 9
#Code

def func(record):
    if record == 0:
        return 1
    elif record == 1:
        return 2
    return 0

def solution9(recordA, recordB):
    cnt = 0
    for i in range(len(recordA)):
        if recordA[i] == recordB[i]:
            continue
        elif recordA[i] == func(recordB[i]):
            cnt = cnt + 3
        else:
            cnt = max(0, cnt - 1)
    return cnt

#The following is code to output testcase. The code below is correct and you shall correct solution function.
recordA = [2,0,0,0,0,0,1,1,0,0]
recordB = [0,0,0,0,2,2,0,2,2,2]
ret = solution9(recordA, recordB)


#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")

#Problem 10
#Code

def solution10(prices):
    INF = 1000000001;
    tmp = INF
    answer = -INF
    for price in prices:
        if tmp != INF:
            answer = max(answer, price - tmp)
        tmp = min(tmp, price)
    return answer

#The following is code to output testcase. The code below is correct and you shall correct solution function.
prices1 = [1, 2, 3];
ret1 = solution10(prices1);

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
prices2 = [3, 1];
ret2 = solution10(prices2);

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")
