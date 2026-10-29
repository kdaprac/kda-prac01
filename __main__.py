import random
import add, minus, multiplication, division

if __name__ == "__main__":    
    while True:
        a = random.randint(0, 10)
        b = random.randint(0, 10)

        option = input("원하는 계산 (+, -, *, /) (종료: 0): ")

        if option == "+":
            res = add.add(a, b)
        elif option == "-":
            res = minus.minus(a, b)
        elif option == "*":
            res = multiplication.multiply(a, b)
        elif option == "/":
            try:
                res = division.division(a, b)
            except ValueError as e:
                print(f"오류: {e}")
                continue
        elif option == "0":
            break
        else:
            print("잘못된 입력입니다")
            continue
        print(f"{a} {option} {b} = {res:.2f}")