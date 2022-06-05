from math import *
from Mode1_funcs.md1_integral import integral
from Mode1_funcs import func_help
from sys import exit
import datetime
'''
mode 1
기본 연산 모듈
파일 입력 가능
'''


def mode1(filename):
    # integral = md1_integral.integral
    f = open(filename, "a")
    ans = None
    date = str(datetime.datetime.now()).split()
    f.write(f"\n{date[0]}\n\n")  # 출력파일에 날짜 적기

    print('''
==========================================================================
    일반 연산 모드
    **사용가능한 함수들의 목록과 예시를 보려면 help를 입력**
    
    함수 앞에 바로 숫자를 쓰지 않도록 하십시오 (ex. 2cos -> 2 * cos)
    로그는 log(x, base)로 작성, base를 쓰지 않으면 자연로그(ln)로 계산합니다
    삼각함수의 각도 단위는 입출력 모두 radian 입니다
    
    0을 입력할 시 프로그램 종료
    반드시 형식에 맞게 입력해야 합니다
        
    입력 예시
    >> 55 + (2^4 - 3) * 4 + ans
    >> 2 * log(3) - 3 * cos(pi)
    >> 3 * root(56 + 23) + 5 * log(5, 10)
    >> integral((0, 3), 'x^3 + 2x^2 - 8x + 2')
==========================================================================
    ''')

    while True:
        expression = input(">> ").strip()

        if expression == '0':
            print("""
==========================================================================
                            프로그램 종료
==========================================================================
            """)
            f.close()
            exit(0)

        if expression.lower() == 'help':
            func_help.func_help()
            continue

        if expression.lower() == 'ans':
            if ans is None:
                print("이전의 계산값이 없습니다")
                print()
                continue
            else:
                print(ans)
                print()
                continue

        # eval 내에서 돌아가도록 expression 수정
        exp = make_beautiful_exp(expression)
        # print(exp)

        try:
            temp_ans = eval(exp)
            ans = round(float(temp_ans), 9)
        except:
            print("잘못된 입력")
            print()
            continue

        print(ans)
        print()
        f.write(f"{expression}  >>  {ans}\n")    # 계산이 정상적으로 됐을 때에만 출력파일에 적힘


def mode1_file_input(out_file_name):
    print("""
=====================================================
    파일 입력 모드
    입력 수식들이 모두 형식에 맞게 작성되어야 합니다
=====================================================
    """)

    input_expressions: list = get_inputfile()
    print()

    f = open(out_file_name, "a")
    ans = None
    date = str(datetime.datetime.now()).split()
    f.write(f"\n{date[0]}\n\n")    # 출력파일에 날짜 넣기

    for expression in input_expressions:
        expression = expression.strip()

        # eval 내에서 돌아가도록 expression 수정
        exp = make_beautiful_exp(expression)
        print(exp)

        try:
            temp_ans = eval(exp)
            ans = round(float(temp_ans), 9)
        except:
            print("잘못된 입력")
            print()
            continue

        print(ans)
        print()
        f.write(f"{expression}  >>  {ans}\n")

    f.close()


def make_beautiful_exp(expression) -> str:
    expression = expression.replace('root', 'sqrt').replace('ln', 'log').replace('^', '**')
    return expression


def get_inputfile():
    while True:
        fname = input("입력파일 이름(~~.txt) : ").strip()

        try:
            f = open(fname, "r")
        except:
            print("존재하지 않는 파일입니다.")
            continue

        exps = f.readlines()
        return exps


# mode1_file_input('out.txt')
if __name__ == '__main__':
    mode1('out.txt')
