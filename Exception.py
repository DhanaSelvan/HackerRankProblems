Test_case = int(input())
for i in range(Test_case):
    try:
        a, b = map(int, input().split(" "))
        result = a//b
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)