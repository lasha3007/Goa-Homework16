def solution(number):
    num=0
    for i in range (number):
        if i%3==0 or i%5==0:
            num=num+i
    return num