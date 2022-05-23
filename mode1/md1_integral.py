from math import *

# 참고.py 활용해서 인테그랄 다시 작성
# integral(2, 5)(x^3 + 2x^2 - 8x + 2)

'''
integral(2, 5)(x^3 + 2x^2 - 8x + 2) -> [inte~, '2, 5', 'x^3 ~~'] (괄호기준 3등분)

'''


def integral(input_func):
    # 100C2
    input_func = input_func.replace(')', '(').replace("((", "(")
    input_func = input_func.split("(")    # input을 괄호기준으로 분리 위해 다 '('로 바꿨음 -> input 3개로 분리
    # input_func = ['integral', '2, 5', 'x^3 + 2x^2 - 8x + 2', '']

    # 범위 a 부터 b 까지
    a, b = eval(input_func[1])
    if a > b:
        a, b = b, a
    # a = 2, b = 5

    # 계산식 수정
    func = input_func[2]
    func = func.replace("^", "**")    # eval 사용 시 ^가 비트연산자로 인식되므로 **로 바꿔서 지수표현으로 수정

    # x 앞에 숫자가 있어도 돌아가도록 수정 (x**3 + 2x**2 - 8x + 2)

    index = -1
    x_index = []    # x의 위치 찾아서 저장할 리스트

    while True:
        index = func.find('x', index + 1)
        if index == -1:
            break
        else:
            x_index.append(index)

    plus_index = 0    # 문자를 추가할거니까 추가한 만큼 인덱스에 더할 값
    for ind in x_index:
        if func[ind - 1 + plus_index].isdigit() and ind:
            func = func[:ind + plus_index] + ' * ' + func[ind + plus_index:]
            plus_index += 3

    # print(func)

    n = 5000 * (b - a)    # 범위를 n등분
    s = 0    # 넓이 총합

    for k in range(1, n):
        x = round(a + k / n, 9)
        s += x_area(func, x, n)

    print(s)


def x_area(func, x, n):    # n등분한 사각형의 넓이
    func = func.replace('x', '(' + str(x) + ')')
    area = eval(func) / n
    # print(area)

    return round(area, 9)


if __name__ == '__main__':
    integral('integral(2, 5)(x^3 + 2x^2 - 8x + 2)')
    integral('integral(0, pi)(cos(2x) + 2)')
    # integral('integral(0, 1)(x^2)')