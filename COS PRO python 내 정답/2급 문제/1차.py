#Problem 1
#Code
import math
def solution1(shirt_size):
    size_list = [0,0,0,0,0,0]
    for ss in shirt_size:
        if ss == "XS":
            size_list[0] += 1;
        elif ss == "S":
            size_list[1] += 1;
        elif ss == "M":
            size_list[2] += 1;
        elif ss == "L":
            size_list[3] += 1;
        elif ss == "XL":
            size_list[4] += 1;
        elif ss == "XXL":
            size_list[5] += 1;
    return size_list

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution1(shirt_size);

#Press Run button to receive output.
print("Solution1: return value of the function is ", ret, " .")

#Problem 2
#Code
import math
def solution2(price,grade):
    if grade == "S":
        return int(price*0.95)
    elif grade == "G":
        return int(price*0.9)
    elif grade == "V":
        return int(price*0.85)

#The following is code to output testcase.
price1 = 2500
grade1 = "V"
ret1 = solution2(price1, grade1)

#Press Run button to receive output.
print("Solution2: return value of the function is", ret1, ".")
    
price2 = 96900
grade2 = "S"
ret2 = solution2(price2, grade2)

#Press Run button to receive output.
print("Solution2: return value of the function is", ret2, ".")

#Problem 3
#Code
def func_a(month,day):
    month_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(month):
        total += month_list[i]
    total += day
    return total-1

def solution3(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total

#The following is code to output testcase.
start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution3(start_month, start_day, end_month, end_day)

#Press Run button to receive output.
print("Solution3: return value of the function is", ret, ".")

#Problem 4
#Code
def func_a4(arr):
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1
    return counter

def func_b4(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c4(arr):
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution4(arr):
    counter = func_a4(arr)
    max_cnt = func_b4(counter)
    min_cnt = func_c4(counter)
    return max_cnt // min_cnt

#The following is code to output testcase.
arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution4(arr)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")

#Problem 5
#Code
def solution5(arr):
    left, right = 0, len(arr)-1
    while left<len(arr)/2:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

#The following is code to output testcase.
arr = [1, 4, 2, 3]
ret = solution5(arr)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")

#Problem 6
#Code
def solution6(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        while current != 0:
            if current%10 == 3 or current%10 == 6 or current%10 == 9:
                count += 1
            current = current // 10
    return count

#The following is code to output testcase.
number = 40
ret = solution6(number)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")

#Problem 7
#Code
def solution7(scores):
    count = 0
    for s in scores:
        if 650 <= s and s < 800:
            count += 1
    return count

#The following is code to output testcase. The code below is correct and you shall correct solution function.
scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution7(scores)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")

#Problem 8
#Code
def solution8(sentence):
    str = ''
    for c in sentence:
        if c != '.' and c != ' ':
            str += c
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size- 1 - i]:
            return False
    return True


#The following is code to output testcase. The code below is correct and you shall correct solution function.
sentence1 = "never odd or even."
ret1 = solution8(sentence1)

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
sentence2 = "palindrome"
ret2 = solution8(sentence2)

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")

#Problem 9
#Code
def solution9(characters):
    result = ""
    result += characters[0]
    for i in range(1,len(characters)):
        if characters[i - 1] != characters[i]:
            result += characters[i]
    return result

#The following is code to output testcase. The code below is correct and you shall correct solution function.
characters = "senteeeencccccceeee"
ret = solution9(characters)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")

#Problem 10
#Code
def solution(data):
    total = sum(data)
    average = total/len(data)
    cnt = 0
    for d in data:
        if d <= average:
            cnt += 1
    return cnt


#The following is code to output testcase. The code below is correct and you shall correct solution function.
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret1 = solution(data1)

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
ret2 = solution(data2)

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")
