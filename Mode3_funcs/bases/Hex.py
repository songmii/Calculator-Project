def hex_calc(exp):
    # hex_calc(exp)

    # 123ABBC / C
    # 123ABBC

    # 123RT 같은거 걸러야함
    operators = ['+', '-', '*', '/']

    # exp를 eval 안에서 돌아가도록 변경
    exp = exp.replace(' ', '').lower()

    # 연산자들 인덱스 찾기
    operator_index = [i for i in range(len(exp)) if exp[i] in operators]
    # print(operator_index)

    # 각 숫자 앞에 '0x' 삽입
    plus_count = 0
    for i in operator_index:
        if i == 0:    # -123abc
            exp = exp[i] + '0x' + exp[i + 1:]
            plus_count += 2

        else:
            exp = exp[:i + plus_count + 1] + '0x' + exp[i + plus_count + 1:]
            plus_count += 2

    if exp[0].isdigit() or exp[0] in ['a', 'b', 'c', 'd', 'e', 'f']:
        exp = '0x' + exp

    # 계산
    try:
        ans = eval(exp)
        # print(ans)
        if not (type(ans) is int or type(ans) is float):
            raise Exception
    except:
        print("53 잘못된 입력")
        return None

    if int(ans) == ans:
        return hex(int(ans))[2:]
    else:
        print("계산값이 소수이므로 사용할 수 없음")
        return None


# print(hex_calc('12ABC + acf / 1'))
