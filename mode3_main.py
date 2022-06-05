# mode 3 : base n
from Mode3_funcs.bases.Bin import bin_calc
from Mode3_funcs.bases.Oct import oct_calc
from Mode3_funcs.bases.Hex import hex_calc
from Mode3_funcs.bases.Dec import dec_calc
from Mode3_funcs.bases.BaseChange import change
import datetime


def mode3(filename):
    print('''
=====================================================
        Base-N 모드에서는 소숫점 입력이 안됩니다.
        분수, 지수도 입력할 수 없습니다.
=====================================================\n''')
    ans = None
    change_lst = ['dec', 'bin', 'oct', 'hex']
    fout = open(filename, "w")

    date = str(datetime.datetime.now()).split()
    fout.write(f"\n======{date[0]}======\n\n")    # 출력파일에 날짜 적기

    while True:
        print("사용할 진법 입력(0 입력 시 프로그램 종료)")
        base_n = input(" 1. Bin(2)   2. Oct(8)   3. Hex(16)   4. Dec(10): ").strip()
        print()

        if base_n == '1':    # bin
            ans = None
            print("""
-----------------------------------------------------------------------
    base 변경 필요 시 'change' 입력
    계산결과 base 변경 필요 시 'Dec' or 'Bin' or 'Oct' or 'Hex' 입력
    입력 예시 >> 1010 + 10001 * 100
-----------------------------------------------------------------------""")
            while True:
                # print("--base 변경 필요 시 'change' 입력--")
                # print("--계산결과 base 변경 필요 시 'Dec' or 'Bin' or 'Oct' or 'Hex' 입력--")
                exp = input("(base:2) 계산할 식 입력 >> ").strip().lower()
                # 1001010001
                if exp == '':
                    continue

                if exp == 'change':
                    print()
                    break    # line 22 로 돌아가서 base_n 다시 입력받음

                elif exp in change_lst:
                    if ans:
                        fout.write(f"{ans} >> ")
                    else:
                        print("이전의 계산값 존재하지 않음")
                        continue

                    temp_ans = change(ans, int(base_n), change_lst.index(exp))
                    # ans의 base를 바꾼 값을 temp_ans에 넣어 ans는 바뀌지 않게 함
                    if temp_ans:    # temp_ans가 None이 아니면
                        print(temp_ans)
                        print()
                        fout.write(f"{temp_ans}\n")
                        continue

                temp_ans = bin_calc(exp)
                '''
                exp 안에는 str이 섞여있을수도
                -> dec_to_bin 함수 안에서 검열
                exp가 이상할 시 ans = None
                '''

                if temp_ans:    # temp_ans가 정상값이어야 ans값이 바뀜
                    ans = temp_ans
                    print(ans)
                    print()
                    fout.write(f"{exp} >> {ans}\n")

        elif base_n == '2':    # oct
            ans = None
            print("""
-----------------------------------------------------------------------
    base 변경 필요 시 'change' 입력
    계산결과 base 변경 필요 시 'Dec' or 'Bin' or 'Oct' or 'Hex' 입력
    입력 예시 >> 1233 * 12 - 357
-----------------------------------------------------------------------""")

            while True:
                exp = input("(base:8) 계산할 식 입력 : ").strip().lower()

                if exp == '':
                    continue

                if exp == 'change':
                    print()
                    break    # line 11 로 돌아가서 base_n 다시 입력받음

                elif exp in change_lst:
                    # print(change(ans, int(base_n), change_lst.index(exp)))
                    if ans:
                        fout.write(f"{ans} >> ")
                    else:
                        print("이전의 계산값 존재하지 않음")
                        continue

                    temp_ans = change(ans, int(base_n), change_lst.index(exp))
                    if temp_ans:
                        print(temp_ans)
                        print()
                        fout.write(f"{temp_ans}\n")
                        continue

                temp_ans = oct_calc(exp)    # 0o~~~

                if temp_ans:
                    ans = temp_ans
                    print(ans)
                    print()
                    fout.write(f"{exp} >> {ans}\n")

        elif base_n == '3':  # hex
            ans = None
            print("""
-----------------------------------------------------------------------
    base 변경 필요 시 'change' 입력
    계산결과 base 변경 필요 시 'Dec' or 'Bin' or 'Oct' or 'Hex' 입력
    입력 예시 >> 12ABC + acf / 1
-----------------------------------------------------------------------""")
            while True:
                exp = input("(base:16) 계산할 식 입력 : ").strip().lower()

                if exp == '':
                    continue

                if exp == 'change':
                    print()
                    break  # line 11 로 돌아가서 base_n 다시 입력받음

                elif exp in change_lst:
                    if ans:
                        fout.write(f"{ans} >> ")
                    else:
                        print("이전의 계산값 존재하지 않음")
                        continue

                    temp_ans = change(ans, int(base_n), change_lst.index(exp))
                    if temp_ans:
                        print(temp_ans)
                        print()
                        fout.write(f"{temp_ans}\n")
                        continue

                temp_ans = hex_calc(exp)

                if temp_ans:
                    ans = temp_ans
                    print(ans)
                    print()
                    fout.write(f"{exp} >> {ans}\n")

        elif base_n == '4':
            ans = None
            print("""
-----------------------------------------------------------------------
    base 변경 필요 시 'change' 입력
    계산결과 base 변경 필요 시 'Dec' or 'Bin' or 'Oct' or 'Hex' 입력
    입력 예시 >> 222 / 2 + 1024
-----------------------------------------------------------------------""")
            while True:
                exp = input("(base:10) 계산할 식 입력 : ").strip().lower()

                if exp == '':
                    continue

                if exp == 'change':
                    print()
                    break  # line 22 로 돌아가서 base_n 다시 입력받음

                elif exp in change_lst:
                    if ans:
                        fout.write(f"{ans} >> ")
                    else:
                        print("이전의 계산값 존재하지 않음")
                        continue

                    temp_ans = change(ans, int(base_n), change_lst.index(exp))
                    if temp_ans:
                        print(temp_ans)
                        print()
                        fout.write(f"{temp_ans}\n")
                        continue

                temp_ans = dec_calc(exp)

                if temp_ans:
                    ans = temp_ans
                    print(ans)
                    print()
                    fout.write(f"{exp} >> {ans}\n")

        elif base_n == '0':
            print("\n===== 프로그램 종료 =====")
            fout.close()
            break

        else:
            print("wrong input, try again.")
            print()


if __name__ == '__main__':
    mode3('out.txt')
