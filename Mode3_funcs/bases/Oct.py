# Base-N 모드에서는 소숫점 입력이 안됩니다. 분수, 지수도 입력할 수 없습니다.

def oct_calc(exp: str):

    # 1234 * 567
    if exp[-1].isdigit() is False:
        print("26 잘못된 입력")
        return None

    exp = exp.replace(" ", "")

    # 연산자들 인덱스 찾기
    operator_index = [i for i in range(len(exp)) if exp[i].isdigit() is False]

    plus_count = 0
    for i in operator_index:
        if i == 0:
            exp = exp[i] + '0o' + exp[i+1:]
            plus_count += 2
        else:
            exp = exp[:i + plus_count + 1] + '0o' + exp[i + plus_count + 1:]
            plus_count += 2

    if exp[0].isdigit():
        exp = '0o' + exp

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
        return oct(int(ans))[2:]
    else:
        print("계산값이 소수이므로 사용할 수 없음")
        return None


# print(dec_to_oct('1234 / 7'))