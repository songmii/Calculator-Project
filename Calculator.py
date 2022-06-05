# 계산기 프로젝트 메인파일
import mode1
import mode2
import mode3
import mode4
import mode5


def main():
    file_print: bool = False
    print("~~안내문구~~")

    print("""
=======================================
            모드 선택
        1. 일반 연산 모드
        2. 복소수 연산 모드
        3. BASE-N 모드
        4. 방정식(equation) 모드
        5. MATRIX 모드
=======================================""")

    while True:
        mode = input(">> ").strip()

        if mode == '1':
            print(""" 입력 형식 >> 1. 직접입력    2. 파일입력""")
            input_form = input("입력 형식 >> ").strip()

            if input_form == '1':
                # mode1('filename')
                mode1.mode1.mode1('filename')
                break

            elif input_form == '2':
                # mode1_file_input('filename')
                mode1.mode1.mode1_file_input('filename')
                break
            # 그 이외에 예외처리하기

        elif mode == '2':
            mode2.mode2.mode2('filename')
            break

        elif mode == '3':
            mode3.mode3.mode3('filename')
            break

        elif mode == '4':
            mode4.mode4('filename')
            break

        elif mode == '5':
            pass
            mode5.mode5('filename')

        else:
            print("잘못된 입력입니다.")


if __name__ == '__main__':
    main()
