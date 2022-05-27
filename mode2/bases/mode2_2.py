from cmath import polar
from math import degrees
# 극좌표 형식으로 출력


def get_polar():
    print("(출력 형식 변경 필요 시 아무것도 입력하지 않고 엔터)")
    exp = input("r∠ɵ >> ").strip()
    # exp = (10+i)(i*2)

    if exp == '':
        return None

    # 괄호가 붙어있을 때 eval이 인식 못하고 에러가 발생하므로 곱하기로 수정
    exp = exp.replace(")(", ")*(").replace("i", "j")
    # exp = (10+j)*(j*2)

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
    # print(exp)

    try:
        exp_cmplx = eval(exp)
    except:
        print("잘못된 입력")
        return 'wrong'

    ans = list(polar(exp_cmplx))
    ans[1] = round(degrees(ans[1]), 1)
    ans[0] = round(ans[0], 9)

    return ans


if __name__ == '__main__':
    get_polar()