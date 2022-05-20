# Base-N 모드에서는 소숫점 입력이 안됩니다. 분수, 지수도 입력할 수 없습니다.

def dec_to_oct(exp):
    # 200 + 36 / 2
    try:
        exp = eval(exp)
    except:
        print("wrong input.")
        return None

    if isinstance(exp, float):
        if exp.is_integer() is False:
            print("Math Error")
            return None

    # print(f"ans = {int(exp):b}")

    return oct(int(exp))