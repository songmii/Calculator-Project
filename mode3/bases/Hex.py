def dec_to_hex(exp):
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

    return hex(int(exp))