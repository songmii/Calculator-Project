def change(ans, from_base, to_index):
    if ans is None:
        return None

    # ans를 10진수로 변경 후 n-base로 변경
    print(f"{ans} = ", end='')
    if from_base == 1:    # 원래 2진수
        ans = int(ans, 2)
    elif from_base == 2:    # 원래 8진수
        ans = int(ans, 8)
    elif from_base == 3:    # 원래 16진수
        ans = int(ans, 16)
    elif from_base == 4:   # 원래 10진수
        ans = int(ans)

    if to_index == 0:    # 10진수로 변경
        return ans
    elif to_index == 1:    # 2진수로 변경
        return bin(ans)[2:]
    elif to_index == 2:
        return oct(ans)[2:]
    elif to_index == 3:
        return hex(ans)[2:]

# print(change('0b10110', 1, 2))
