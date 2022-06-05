# a + bi 형식으로 출력
from cmath import rect
from math import radians


def get_i(ans) -> (complex, str):
    print("(출력 형식 변경 필요 시 아무것도 입력하지 않고 엔터)")
    exp = input("a + bi >> ").strip()
    original_exp = exp
    # exp = (10+i)(i*2)

    if exp == '':
        return None, None

    if exp.lower() == 'ans':
        return 'ans', exp

    # 괄호가 붙어있을 때 eval이 인식 못하고 에러가 발생하므로 곱하기로 수정
    exp = exp.replace(")(", ")*(").replace("i", "j").replace("^", "**")


    # 연산 두 가지 형태가 한번에 들어오면?
    '''
    (10 + j5 + 3∠40) / (-3 + j4) + 10∠30 + j5
    는 어떻게 처리?
    (10∠10)(5.34∠2.88)
    '''
    # 입력을 r∠ɵ 형태로 한 경우
    if '∠' in exp:
        try:    # (40∠50 + 20.35∠-30) ^ 0.5    ans + 20∠-30.234
            exp = exp.split('∠')
            r = eval(exp[0])
            deg = eval(exp[1])

            # exp = exp.split()
            # for p in exp:

        except:
            print("잘못된 입력")
            return "wrong", None

        deg_to_phi = radians(deg)
        ans = rect(r, deg_to_phi)    # type : complex

        return ans, original_exp

    else:    # 입력이 a+bi형태인 경우
        # j 인식 못하므로 1j로 바꿈
        j_index = [i for i in range(len(exp)) if exp[i] == 'j']

        plus_count = 0
        for ind in j_index:
            ind += plus_count

            if ind == 0:
                exp = '1' + exp
                plus_count += 1

            elif exp[ind-1].isdigit() is False:
                exp = exp[:ind] + '1' + exp[ind:]
                plus_count += 1
        # j 인식 못하므로 1j로 바꿈

        try:
            ans = eval(exp)
            # print(ans)
        except:
            print("잘못된 입력")
            return 'wrong', None

        return ans, original_exp


def polar_to_i(ans):
    if type(ans) == list:
        # [10.049875621, 5.7]
        ans[1] = radians(ans[1])
        new_ans = rect(ans[0], ans[1])    # complex
        return new_ans

    else:
        return ans


if __name__ == '__main__':
    print(type(get_i()))
