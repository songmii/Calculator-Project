# 계산기 프로젝트 메인파일
import mode1_main
import mode2_main
import mode3_main
import mode4_main
import mode5_main


def main():
    print("\nSTART PYTHON CALCULATOR\n")
    print("출력 파일 지정 -> 모드 선택 -> 연산\n")
    fname = get_filename()

    print("""
=======================================
            모드 선택
        1. 일반 연산 모드
        2. 복소수 연산 모드
        3. BASE-N 모드
        4. equation(방정식) 모드
        5. MATRIX(행렬) 모드
=======================================""")

    while True:
        mode = input(">> ").strip()

        if mode == '1':
            print(""" 입력 형식 >> 1. 직접입력    2. 파일입력""")
            input_form = input("입력 형식 >> ").strip()

            if input_form == '1':
                mode1_main.mode1(fname)
                break

            elif input_form == '2':
                mode1_main.mode1_file_input(fname)
                break
            # 그 이외에 예외처리하기

            else:
                print("1 혹은 2 입력\n")

        elif mode == '2':
            mode2_main.mode2(fname)
            break

        elif mode == '3':
            mode3_main.mode3(fname)
            break

        elif mode == '4':
            mode4_main.mode4(fname)
            break

        elif mode == '5':
            mode5_main.mode5(fname)
            break

        else:
            print("잘못된 입력입니다.")


def get_filename():
    while True:
        fname = input("출력파일 이름 입력(~~.txt) : ").strip()
        if fname.endswith('.txt'):
            return fname
        else:
            print("파일명이 .txt로 끝나야 합니다.\n")


if __name__ == '__main__':
    main()
