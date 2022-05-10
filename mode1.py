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
    print(calc)

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
    print(calc)

    x = float(calc[1])    # float(calc_mode1())
    # 각 라디안으로 통일
    ans = math.sin(x)

    return str(round(ans, 9))


def cos(calc: str) -> str:
    pass


# print(log('log(10)(10)'))
# print(ln('ln(2.7)'))
# print(sin('sin(1.5)'))
