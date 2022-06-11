from math import *


def integral(scope: tuple, input_func: str):
    if type(input_func) is not str:
        print("적분의 입력형식이 맞지 않습니다.")
        return None

    is_minus = False

    # 범위 a 부터 b 까지
    a, b = eval(str(scope))
    if a > b:
        a, b = b, a
        is_minus = True

    # 계산식 수정
    func = make_beautiful_func(input_func)
    # print(f"func : {func}")

    # 구분구적법 시작
    n = int(10000 * (b - a))   # 1칸을 1만등분
    s = 0    # 넓이 총합

    try:
        for k in range(1, n+1):
            x = round(a + ((1 / 10000) * k), 9)

            s += x_area(func, x)
    except:
        print("적분의 입력에 문제가 있습니다.")
        return None

    s = round(s, 2)   # 소수점 뒤로갈수록 오차가 늘어나서 2자리까지만 표시

    if is_minus:
        return float("-{s}")
    else:
        return s


def x_area(func, x):    # n등분한 사각형의 넓이
    func = func.replace('x', '(' + str(x) + ')')
    area = eval(func) / 10000
    # print(area)

    return round(area, 9)


def make_beautiful_func(input_func: str):
    func = input_func.replace("^", "**")  # eval 사용 시 ^가 비트연산자로 인식되므로 **로 바꿔서 지수표현으로 수정
    func = func.replace("root", "sqrt")

    # x 앞에 숫자가 있어도 돌아가도록 수정 (x**3 + 2x**2 - 8x + 2)
    x_index = [i for i in range(len(func)) if func[i] == 'x']  # x의 위치

    plus_index = 0  # 문자를 추가할거니까 추가한 만큼 인덱스에 더할 값
    for ind in x_index:
        ind += plus_index
        if func[ind - 1].isdigit() and ind:
            func = func[:ind] + ' * ' + func[ind:]
            plus_index += 3

    return func


if __name__ == '__main__':
    # print(integral((5, 2), 'x^3 + 2x^2 - 8x + 2'))
    # # main 함수에서 2 * cos, 3 * log()로 작성해야 한다고 안내
    # print(integral((0, pi), 'cos(2x) + 2'))
    # print(integral((1, 3), 'log(x, 10)'))
    # print(integral((2, 3), 'acos(x)'))
    # print(integral((1, 5), '5 * sqrt(x + 2)'))
    # print(integral((1, 5), 5 * sqrt(x + 2)))
    pass