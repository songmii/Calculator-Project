# mode 3 : base n
from bases.Bin import dec_to_bin
from bases.Oct import dec_to_oct
from bases.Hex import dec_to_hex
from bases.BaseChange import change


def mode3():
    print('Base-N 모드에서는 소숫점 입력이 안됩니다. 분수, 지수도 입력할 수 없습니다.')
    ans = 0
    change_lst = ['Dec', 'Bin', 'Oct', 'Hex']

    while True:
        print("사용할 진법 입력(0 입력 시 프로그램 종료) : ")
        base_n = input(" 1. Bin(2)   2. Oct(8)   3. Hex(16) : ").strip()
        print()

        if base_n == '1':    # bin
            while True:
                print("--base 변경 필요 시 'change' 입력--")
                print("--계산결과 base 변경 필요 시 'Dec' or 'Bin' or 'Oct' or 'Hex' 입력--")
                exp = input("(base:2) 계산할 식 입력 : ")

                if exp == 'change':
                    print()
                    break    # line 11 로 돌아가서 base_n 다시 입력받음
                elif exp in change_lst:
                    print(change(ans, int(base_n), change_lst.index(exp)))
                    print()
                    continue

                ans = dec_to_bin(exp)
                '''
                exp 안에는 str이 섞여있을수도
                -> dec_to_bin 함수 안에서 검열
                exp가 이상할 시 ans = None
                '''

                if ans:
                    print(ans[2:])    # ans = 0b~~ 이므로 0b 이후부터 출력
                    print()

        elif base_n == '2':    # oct
            while True:
                print("--base 변경 필요 시 'change' 입력--")
                print("--계산결과 base 변경 필요 시 'Dec' or 'Bin' or 'Oct' or 'Hex' 입력--")
                exp = input("(base:8) 계산할 식 입력 : ")

                if exp == 'change':
                    print()
                    break    # line 11 로 돌아가서 base_n 다시 입력받음
                elif exp in change_lst:
                    print(change(ans, int(base_n), change_lst.index(exp)))
                    print()
                    continue

                ans = dec_to_oct(exp)

                if ans:
                    print(ans[2:])
                    print()

        elif base_n == '3':  # hex
            while True:
                print("--base 변경 필요 시 'change' 입력--")
                print("--계산결과 base 변경 필요 시 'Dec' or 'Bin' or 'Oct' or 'Hex' 입력--")
                exp = input("(base:16) 계산할 식 입력 : ")

                if exp == 'change':
                    print()
                    break  # line 11 로 돌아가서 base_n 다시 입력받음
                elif exp in change_lst:
                    print(change(ans, int(base_n), change_lst.index(exp)))
                    print()
                    continue

                ans = dec_to_hex(exp)

                if ans:
                    print(ans[2:])
                    print()

        elif base_n == '0':
            print("===== 프로그램 종료 =====")
            break

        else:
            print("wrong input, try again.")
            print()
