# Base-N 모드에서는 소숫점 입력이 안됩니다. 분수, 지수도 입력할 수 없습니다.

def bin_calc(exp: str):
    # bin_calc
    # 200 + 36 / 2
    # 11011010+111000
    # int
    #
    # if exp.isdigit():    # 11011010
    #     # if exp.startswith('0'):    # 0으로 시작하면 거르기
    #     #     print("11 잘못된 입력")
    #     #     return None
    #
    #     exp = '0b' + exp
    #     try:    # 0과 1 이외의 숫자가 들어온 경우 거름
    #         ans = eval(exp)
    #     except:
    #         print("18 잘못된 입력")
    #         return None
    #
    #     # exp : '0b11011010'
    #     return exp    # type : str

   # 11011010+111000

    if exp[-1].isdigit() is False:    # 010001+ 같은것 거르기
        print("27 잘못된 입력")
        return None

    exp = exp.replace(' ', '')    # 중간의 공백 제거

    # 연산자들 인덱스 찾기
    operator_index = [i for i in range(len(exp)) if exp[i].isdigit() is False]

    # 각 숫자 앞에 '0b' 삽입
    plus_count = 0
    for i in operator_index:
        if i == 0:
            exp = exp[i] + '0b' + exp[i+1:]
            plus_count += 2

        else:
            exp = exp[:i + plus_count + 1] + '0b' + exp[i + plus_count + 1:]
            plus_count += 2

    if exp[0].isdigit():
        exp = '0b' + exp

    # 계산
    try:
        ans = eval(exp)
        if not (type(ans) is int or type(ans) is float):
            raise Exception
    except:
        print("57 잘못된 입력")
        return None

    if int(ans) == ans:    # ans가 소수이면(1.30은 ok)
        return bin(int(ans))[2:]
    else:
        print("계산값이 소수이므로 사용할 수 없음")
        return None


# print(bin_calc('01011110 + 111'))
