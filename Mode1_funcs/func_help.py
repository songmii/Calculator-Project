def func_help():
    print("""
--------------------------------------------------------------------
연산부호 + , - , * , / 사용
상수로 pi, e 사용가능


[지수와 로그 함수]
지수 표현 시  ^ 기호 사용    ex) 2^3  10^-2
제곱근 표현 시 root 사용    ex)  root(10)  root(16)

로그 표현 시 log(x, base) 형식으로 입력    ex) log(2, 2)  log(5, 10)
base입력하지 않을 시 자연로그(ln)으로 계산    ex)  log(3)  log(e)
ln(x) 사용도 가능


[삼각함수]
cos(x), sin(x), tan(x), acos(x), asin(x), atan(x)
cosh(x), sinh(x), tanh(x), acosh(x), asinh(x), atanh(x) 


[각도 변환]
degrees(x) 는 라디안각 x를 도(degree)로 변환
radians(x)는 각(degree) x를 라디안으로 변환
ex)  cos(radians(90))  degrees(sin(pi / 2))


[적분]
integral((적분범위 a, b), '미지수 x를 포함한 계산식') 형태로 입력 
ex)  integral((0, 3), 'cos(2x) + 2')),  integral((0, 3), 'x^3 + 2x^2 - 8x + 2'))

--------------------------------------------------------------------
""")
