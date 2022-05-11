# 1.
import math

def calc_mode1():
    pass


def log(calc: str) -> str:
    # log(2)(3)
    # log(base)(x)
    # calc = 'log(ln(~))'
    calc = calc.replace(')', "(").replace("((", "(")
    # print(calc)
    calc = calc.split("(")
    base = calc[1]    # base = calc_mode1()
    x = calc[2]     # x = calc_mode1()

    if base == '2':
        ans = math.log2(float(x))    # log(x, 2)보다 정확
    elif base == '10':
        ans = math.log10(float(x))    # log(x, 10)보다 정확
    else:
        ans = math.log(float(x), float(base))

    return str(round(ans, 9))


def ln(calc: str) -> str:
    # ln(23)
    calc = calc.replace(')', "(").replace("((", "(")
    calc = calc.split("(")
    # print(calc)

    x = calc[1]

    ans = math.log(float(x))

    return str(round(ans, 9))


def sin(calc: str) -> str:
    # calc = 'sin(52)'
    # 전역변수로 degree, radian 선언
    # 디폴트로 디그리
    # math.sin(x)가 기본적ㅇ로 라디안이므로 각 변환 필요
    calc = calc.replace(')', "(").replace("((", "(")
    calc = calc.split("(")
    # print(calc)

    x = float(calc[1])    # float(calc_mode1())
    # 각 라디안으로 통일
    ans = math.sin(x)

    return str(round(ans, 9))


def cos(calc: str) -> str:
    calc = calc.replace(')', "(").replace("((", "(")
    calc = calc.split("(")
    # print(calc)

    x = float(calc[1])  # float(calc_mode1())
    # 각 라디안으로 통일
    ans = math.cos(x)

    return str(round(ans, 9))


def tan(calc: str):
    calc = calc.replace(')', "(").replace("((", "(")
    calc = calc.split("(")
    # print(calc)

    x = eval(calc[1])  # float(calc_mode1())
    # 각 라디안으로 통일

    if x == math.pi / 2:
        print("Math Error")
        return 0    # tan(90도)했을 때 어떻게 처리할지??

    ans = math.tan(x)

    return str(round(ans, 9))


def acos(calc: str):
    calc = calc.replace(')', "(").replace("((", "(")
    calc = calc.split("(")
    # print(calc)

    x = eval(calc[1])  # float(calc_mode1())
    # 각 라디안으로 통일

    if -1 <= x <= 1:
        ans = math.acos(x)
    else:
        print("Math Error")
        return None

    return str(round(ans, 9))


def asin(calc: str):
    calc = calc.replace(')', "(").replace("((", "(")
    calc = calc.split("(")
    # print(calc)

    x = eval(calc[1])  # float(calc_mode1())
    # 각 라디안으로 통일

    if -1 <= x <= 1:
        ans = math.asin(x)
    else:
        print("Math Error")
        return None

    return str(round(ans, 9))


def atan(calc: str):
    calc = calc.replace(')', "(").replace("((", "(")
    calc = calc.split("(")
    # print(calc)

    x = eval(calc[1])  # float(calc_mode1())

    # 각 라디안으로 통일
    ans = math.atan(x)

    return str(round(ans, 9))


def cosh(calc: str):
    calc = calc.replace(')', "(").replace("((", "(")
    calc = calc.split("(")
    # print(calc)

    x = eval(calc[1])  # float(calc_mode1())
    # 각 라디안으로 통일

    if -230 <= x <= 230:
        ans = math.cosh(x)
    else:
        print("Math Error")
        return None

    return str(round(ans, 9))


def sinh(calc: str):
    calc = calc.replace(')', "(").replace("((", "(")
    calc = calc.split("(")
    # print(calc)

    x = eval(calc[1])  # float(calc_mode1())
    # 각 라디안으로 통일

    if -230 <= x <= 230:
        ans = math.sinh(x)
    else:
        print("Math Error")
        return None

    return str(round(ans, 9))


def tanh(calc: str):
    calc = calc.replace(')', "(").replace("((", "(")
    calc = calc.split("(")
    # print(calc)

    x = eval(calc[1])  # float(calc_mode1())
    ans = math.tanh(x)

    return str(round(ans, 9))


def acosh(calc: str):
    calc = calc.replace(')', "(").replace("((", "(")
    calc = calc.split("(")
    # print(calc)

    x = eval(calc[1])  # float(calc_mode1())
    if x >= 1:
        ans = math.acosh(x)
    else:
        print("Math Error")
        return None

    return str(round(ans, 9))


def asinh(calc: str):
    calc = calc.replace(')', "(").replace("((", "(")
    calc = calc.split("(")
    # print(calc)

    x = eval(calc[1])  # float(calc_mode1())
    ans = math.asinh(x)

    return str(round(ans, 9))


def atanh(calc: str):
    calc = calc.replace(')', "(").replace("((", "(")
    calc = calc.split("(")
    # print(calc)

    x = eval(calc[1])  # float(calc_mode1())
    if -1 < x < 1:
        ans = math.atanh(x)
    else:
        print("Math Error")
        return None

    return str(round(ans, 9))


def pi(calc):
    # 25pi
    # ( 25pi + 3 -> 괄호는 안들어옴
    if calc.index('pi') == 0:
        # 25pi 같은 경우 '25*pi'를 리턴하도록
        calc = calc.replace('pi', str(round(math.pi, 9)))
    else:
        # 그냥 pi가 들어올경우 숫자로만 바꿔서 리턴
        calc = calc.replace('pi', '*'+str(round(math.pi, 9)))

    return calc


def e(calc):
    # 25e
    if calc.index('e') == 0:
        calc = calc.replace('e', str(round(math.e, 9)))
    else:
        # 그냥 e가 들어올경우 숫자로만 바꿔서 리턴
        calc = calc.replace('e', '*'+str(round(math.e, 9)))

    return calc


def root(calc):
    # root(25 +
    pass


'''TEST CODE'''
# print(log('log(10)(10)'))
# print(ln('ln(2.7)'))
# print(sin('sin(1.5)'))
# print(cos('cos(3.141592)'))
# print(tan('tan(52 + 16)'))
# print(acos('acos(-0.8)'))
# print(atan('atan(2022)'))
# print(cosh('cosh(10)'))
# print(sinh('sinh(10)'))
# print(tanh('tanh(0.3)'))
# print(acosh('acosh(-1)'))
# print(asinh('asinh(20)'))
# print(atanh('atanh(12)'))
# print(pi('1.3pi'))
# print(e('2.71e'))


# eval 내부에 '^'가 있으면 비트연산자로 인식하는듯,,,
# 수식 입력할 때 괄호 양 옆도 공백으로 띄워서 입력하라고 안내하기
