# mode 2 : CMPLX
from bases.mode2_1 import conjg
from bases.mode2_2 import get_polar, i_to_polar
from bases.mode2_3 import get_i, polar_to_i
from sys import exit


def mode2(filename):
    # filename : output file name
    ans = None
    fout = open(filename, "a")

    while True:
        print('''
====================================
        연산 형식 입력 : (0 입력시 프로그램 종료)
        1. conjg(켤레복소수 계산)
        2. r∠ɵ
        3. a+bi
        
        입력 예시
        연산 형식 >> 2
====================================
        ''')
        n = input("연산 형식>> ").strip()
        print()

        if n == '1':
            while True:
                # ans = conjg()
                temp_ans, original_exp = conjg()    # ans에 정상적인 결과값만 저장되도록 ans값을 임시로 저장할 temp_ans 선언

                if temp_ans is None:    # 수식 입력할 때 바로 엔터 누른 경우 -> ans값은 그대로 유지
                    break
                if temp_ans == 'wrong':
                    continue

                ans = temp_ans    # 정상적으로 계산 완료했을 때 ans에 값 저장됨
                print(ans)
                print()
                fout.write(f"{original_exp} >> {ans}\n")

        elif n == '2':
            if ans:    # 출력형식을 변경했을 때 ans값이 있으면 ans를 변경한 출력형식으로 바꿔서 출력 먼저 해줌
                print(f"이전의 ans : {ans} >> ", end='')
                fout.write(f"{ans} >> ")

                ans = i_to_polar(ans)
                print(f"{ans[0]}∠{ans[1]}")
                print()
                fout.write(f"{ans[0]}∠{ans[1]}\n")

            while True:
                temp_ans, original_exp = get_polar()

                if temp_ans is None:
                    break
                if temp_ans == 'wrong':
                    print()
                    continue

                ans = temp_ans
                print(f"{ans[0]}∠{ans[1]}")
                print()
                fout.write(f"{original_exp} >> {ans[0]}∠{ans[1]}\n")

        elif n == '3':
            if ans:    # 출력형식을 변경했을 때 ans값이 있으면 ans를 변경한 출력형식으로 바꿔서 출력 먼저 해줌
                if type(ans) is list:
                    print(f"이전의 ans : {ans[0]}∠{ans[1]} >> ", end='')
                    fout.write(f"{ans[0]}∠{ans[1]} >> ")
                else:
                    print(f"이전의 ans : {ans} >> ", end='')
                    fout.write(f"{ans} >> ")

                ans = polar_to_i(ans)
                print(ans)
                print()
                fout.write(f"{ans}\n")

            while True:
                temp_ans, original_exp = get_i()

                if temp_ans is None:
                    break
                if temp_ans == 'wrong':
                    print()
                    continue

                ans = temp_ans
                print(ans)
                print()
                fout.write(f"{original_exp} >> {ans}\n")

        elif n == '0':
            print('''
====================================
            프로그램 종료
====================================
            ''')
            exit(0)


if __name__ == '__main__':
    mode2('out.txt')
