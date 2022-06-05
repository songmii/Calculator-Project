# 켤레복소수 구하는 함수

def conjg() -> (complex, str):
    print("(출력 형식 변경 필요 시 아무것도 입력하지 않고 엔터)")
    exp = input("Conjg >> ").strip()
    original_exp = exp
    # exp = 23-i

    if exp == '':
        return None, None

    exp = exp.replace("i", "j")    # 입력을 i로 할텐데 파이썬은 i 대신 j 사용하므로 수정
    # exp = (2 - 3j)(5 + 2j)

    exp = exp.replace(")(", ") * (")
    # 괄호가 붙어있을 때 eval이 인식 못하고 에러가 발생하므로 곱하기로 수정

    # j 인식 못하므로 1j로 바꿈
    j_index = [i for i in range(len(exp)) if exp[i] == 'j']

    '''
    ((5 + j2)(-1 + j4) - 5∠60)
    어떻게 계산할건지??
    '''


    plus_count = 0
    for ind in j_index:
        ind += plus_count

        if ind == 0:
            exp = '1' + exp
            plus_count += 1

        elif exp[ind - 1].isdigit() is False:
            exp = exp[:ind] + '1' + exp[ind:]
            plus_count += 1

    try:
        exp_cmplx = eval(exp)
    except:
        print("잘못된 입력")
        return 'wrong', None

    return exp_cmplx.conjugate(), original_exp    # 켤레복소수 리턴하는 메소드


if __name__ == '__main__':
    print(conjg())
