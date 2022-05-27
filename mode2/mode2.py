# mode 2 : CMPLX
from mode2.bases.mode2_1 import conjg
from mode2.bases.mode2_2 import get_polar
from mode2.bases.mode2_3 import get_i
from sys import exit


def mode2():
    ans = None

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
                ans = conjg()
                # 앞에 숫자가 없고 그냥 j면 에러뜨므로 수정

                if ans is None:
                    break
                if ans == 'wrong':
                    continue

                else:
                    print(ans)
                    print()

        elif n == '2':
            while True:
                ans = get_polar()

                if ans is None:
                    break
                if ans == 'wrong':
                    continue

                else:
                    print(f"{ans[0]}∠{ans[1]}")
                    print()

        elif n == '3':
            while True:
                ans = get_i()

                if ans is None:
                    break
                if ans == 'wrong':
                    continue

        elif n == '0':
            print('''
====================================
            프로그램 종료
====================================
            ''')
            exit(0)


if __name__ == '__main__':
    mode2()
