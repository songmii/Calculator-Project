from cmath import rect
from math import radians
# 켤레복소수 구하는 함수

def conjg() -> (complex, str):
    print("(출력 형식 변경 필요 시 아무것도 입력하지 않고 엔터)")
    exp = input("Conjg >> ").strip()
    original_exp = exp
    # exp = 23-i

    if exp == '':
        return None, None

    # exp = exp.replace("i", "j")    # 입력을 i로 할텐데 파이썬은 i 대신 j 사용하므로 수정
    # # exp = (2 - 3j)(5 + 2j)
    #
    # exp = exp.replace(")(", ") * (")
    # # 괄호가 붙어있을 때 eval이 인식 못하고 에러가 발생하므로 곱하기로 수정
    #
    # # j 인식 못하므로 1j로 바꿈
    # j_index = [i for i in range(len(exp)) if exp[i] == 'j']
    #
    # plus_count = 0
    # for ind in j_index:
    #     ind += plus_count
    #
    #     if ind == 0:
    #         exp = '1' + exp
    #         plus_count += 1
    #
    #     elif exp[ind - 1].isdigit() is False:
    #         exp = exp[:ind] + '1' + exp[ind:]
    #         plus_count += 1

    exp = make_beautiful_exp(exp)

    try:
        exp_cmplx = eval(exp)
    except:
        print("잘못된 입력")
        return 'wrong', None

    return exp_cmplx.conjugate(), original_exp    # 켤레복소수 리턴하는 메소드


def make_beautiful_exp(exp):
    lst_exp = list(exp)
    # print(lst_exp)

    polar_index = [i for i in range(len(lst_exp)) if lst_exp[i] == '∠']
    # print(polar_index)  # [2, 9]

    before_turn_index = []  # '∠' 옆에 숫자까지의 인덱스 리스트
    for i in polar_index:
        a, b = i - 1, i + 1
        while lst_exp[a].isdigit() or lst_exp[a] == '-' or lst_exp[a] == '.':
            if a < 0:
                break
            a -= 1
        a += 1

        while lst_exp[b].isdigit() or lst_exp[b] == '-' or lst_exp[b] == '.':
            if b == len(lst_exp) - 1:
                b += 1
                break
            b += 1
        b -= 1

        before_turn_index.append((a, b))

    # print(before_turn_index)

    # lst_exp에서 범위만큼을 가져와서 변환 계산, 리스트에 넣기
    after_turn_lst = []
    for scope in before_turn_index:
        a = scope[0]
        b = scope[1]

        temp_exp = ''.join(lst_exp[a:b + 1])
        # print(temp_exp)

        ttemp_exp = temp_exp.split('∠')
        # print(ttemp_exp)

        r = eval(ttemp_exp[0])
        deg = eval(ttemp_exp[1])

        deg_to_phi = radians(deg)
        turn_exp = rect(r, deg_to_phi)  # type : complex

        # print(turn_exp)
        after_turn_lst.append((temp_exp, str(turn_exp)))

    # print(after_turn_lst)

    for turn in after_turn_lst:
        exp = exp.replace(turn[0], turn[1])

    # print(exp)

    # 괄호가 붙어있을 때 eval이 인식 못하고 에러가 발생하므로 곱하기로 수정
    exp = exp.replace(")(", ")*(").replace("i", "j").replace("^", "**")

    # j 인식 못하므로 1j로 바꿈
    j_index = [i for i in range(len(exp)) if exp[i] == 'j']

    plus_count = 0
    for ind in j_index:
        ind += plus_count

        if ind == 0:
            exp = '1' + exp
            plus_count += 1

        elif exp[ind - 1].isdigit() is False:
            exp = exp[:ind] + '1' + exp[ind:]
            plus_count += 1
    # j 인식 못하므로 1j로 바꿈

    # print(exp)
    return exp


if __name__ == '__main__':
    print(conjg())
