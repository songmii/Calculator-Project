# Base-N 모드에서는 소숫점 입력이 안됩니다. 분수, 지수도 입력할 수 없습니다.

def dec_calc(exp: str):
    operators = ['+', '-', '/', '*']
    # 1234 * 5670
    if exp[-1].isdigit() is False:
        print("7 잘못된 입력")
        return None

    exp = exp.replace(" ", "")
    # 연산자들 인덱스 찾기
    operator_index = [i for i in range(len(exp)) if exp[i].isdigit() is False]

    for i in operator_index:
        if exp[i] not in operators:
            print(f"{exp[i]}는 사용할 수 없음")
            return None

    # 계산
    try:
        ans = eval(exp)
        # print(ans)
        if not (type(ans) is int or type(ans) is float):
            raise Exception
    except:
        print("52 잘못된 입력")
        return None

    if int(ans) == ans:
        return int(ans)
    else:
        print("계산값이 소수이므로 사용할 수 없음")
        return None


# print(dec_calc('int'))