import random

arr = [1, 2, 3, 4, 5, 6, 7, 8]
numbers = list(range(1, 9))
random.shuffle(numbers)
flag = 1
turn = 1

def check(nums):
    global flag, turn
    try:  
        num1, num2 = map(str, nums.split(','))
        if nums.startswith(" "):
            print("잘못 입력하셨습니다. 다시 입력해 주세요.")
            print()
            flag = 0
        elif int(num1) in numbers and int(num2) in numbers:
            turn += 1
            flag = 1
            index1 = numbers.index(int(num1))
            index2 = numbers.index(int(num2))
            numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
        else:
            print("잘못 입력하셨습니다. 다시 입력해 주세요.")
            print()
            flag = 0
    except ValueError:
        print("잘못 입력하셨습니다. 다시 입력해 주세요.")
        print()
        flag = 0
    
print("간단 숫자 퍼즐")

while True:

    if arr == numbers:
        print(f"축하합니다! {turn}턴만에 퍼즐을 완성하셨습니다!")
        break

    if flag == 1:
        print(f"Turn {turn}")
        print(numbers)
        print("교환할 두 숫자를 입력>")
        nums = input()
        print()
        check(nums)

    elif flag == 0:
        print("교환할 두 숫자를 입력>")
        nums = input()
        print()
        check(nums)