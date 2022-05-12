def calc_mode1(s1): # s1 : 전체 입력 수식

    list1 = s1.split() # 수식을 띄어쓰기 단위로 나눈 list
    list2 = [] # eval이 되지 않는 부분을 모두 eval이 가능하도록 변경한 list

    for i in range(len(list1)):
        while(True):
            if list1[i] == "(" or list1[i] ==  ")":
                list2.append(list1[i])  #괄호 '(' 또는 ')' 일 경우 그대로 저장
                break

            if list1[i] == "+" or list1[i] ==  "-" or list1[i] == "*" or list1[i] ==  "/":
                list2.append(list1[i])
                break

            try:
                eval(list1[i]) #eval에 바로 통과가 되는 경우('int','float') 그대로 저장
                list2.append(list1[i])
                break

            except:  #eval에서 오류가 생기는 경우 => 함수 호출이 필요한 경우

                try:
                    index_log = list1[i].find("log") #index_log : 'log'가 존재하는 index
                    if index_log > 0: #'log' 앞에 상수가 곱해진 경우
                        list1[i] = list1[i][0:index_log] + "*" + log(list1[i][index_log:])
                    elif index_log == 0: #'log' 앞에 상수가 곱해지지 않은 경우
                        list1[i] =  log(list1[i][index_log:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_ln = list1[i].find("ln")
                    if index_ln > 0:
                        list1[i] = list1[i][0:index_ln] + "*" + ln(list1[i][index_ln:])
                    elif index_ln == 0:
                        list1[i] =  ln(list1[i][index_ln:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_sin = list1[i].find("sin")
                    if index_sin > 0:
                        list1[i] = list1[i][0:index_sin] + "*" + sin(list1[i][index_sin:])
                    elif index_sin == 0:
                        list1[i] =  sin(list1[i][index_sin:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_cos = list1[i].find("cos")
                    if index_cos > 0:
                        list1[i] = list1[i][0:index_cos] + "*" + cos(list1[i][index_cos:])
                    elif index_cos == 0:
                        list1[i] =  cos(list1[i][index_cos:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_tan = list1[i].find("tan")
                    if index_tan > 0:
                        list1[i] = list1[i][0:index_tan] + "*" + tan(list1[i][index_tan:])
                    elif index_tan == 0:
                        list1[i] =  tan(list1[i][index_tan:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_asin = list1[i].find("asin")
                    if index_asin > 0:
                        list1[i] = list1[i][0:index_asin] + "*" + asin(list1[i][index_asin:])
                    elif index_asin == 0:
                        list1[i] =  asin(list1[i][index_asin:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_acos = list1[i].find("acos")
                    if index_acos > 0:
                        list1[i] = list1[i][0:index_acos] + "*" + acos(list1[i][index_acos:])
                    elif index_acos == 0:
                        list1[i] =  acos(list1[i][index_acos:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_atan = list1[i].find("atan")
                    if index_atan > 0:
                        list1[i] = list1[i][0:index_atan] + "*" + atan(list1[i][index_atan:])
                    elif index_atan == 0:
                        list1[i] =  atan(list1[i][index_atan:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_sinh = list1[i].find("sinh")
                    if index_sinh > 0:
                        list1[i] = list1[i][0:index_sinh] + "*" + sinh(list1[i][index_sinh:])
                    elif index_sin == 0:
                        list1[i] =  sinh(list1[i][index_sinh:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_cosh = list1[i].find("cosh")
                    if index_cosh > 0:
                        list1[i] = list1[i][0:index_cosh] + "*" + cosh(list1[i][index_cosh:])
                    elif index_cosh == 0:
                        list1[i] =  cosh(list1[i][index_cosh:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_tanh = list1[i].find("tanh")
                    if index_tanh > 0:
                        list1[i] = list1[i][0:index_tanh] + "*" + tanh(list1[i][index_tanh:])
                    elif index_tanh == 0:
                        list1[i] =  tanh(list1[i][index_tanh:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_asinh = list1[i].find("asinh")
                    if index_asinh > 0:
                        list1[i] = list1[i][0:index_asinh] + "*" + asinh(list1[i][index_asinh:])
                    elif index_asinh == 0:
                        list1[i] =  asinh(list1[i][index_asinhh:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_acosh = list1[i].find("acosh")
                    if index_acosh > 0:
                        list1[i] = list1[i][0:index_acosh] + "*" + acosh(list1[i][index_acosh:])
                    elif index_acosh == 0:
                        list1[i] =  acosh(list1[i][index_acosh:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_atanh = list1[i].find("atanh")
                    if index_atanh > 0:
                        list1[i] = list1[i][0:index_atanh] + "*" + atanh(list1[i][index_atanh:])
                    elif index_atanh == 0:
                        list1[i] =  atanh(list1[i][index_atanh:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_pi = list1[i].find("pi")
                    if index_pi > 0:
                        list1[i] = list1[i][0:index_pi] + "*" + pi(list1[i][index_pi:])
                    elif index_pi == 0:
                        list1[i] =  pi(list1[i][index_pi:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_e = list1[i].find("e")
                    if index_e > 0:
                        list1[i] = list1[i][0:index_e] + "*" + e(list1[i][index_e:])
                    elif index_e == 0:
                        list1[i] =  e(list1[i][index_e:])
                    else:
                        pass
                except:
                    pass

                try:
                    index_root = list1[i].find("root")
                    if index_root > 0:
                        list1[i] = list1[i][0:index_root] + "*" + root(list1[i][index_root:])
                    elif index_root == 0:
                        list1[i] =  root(list1[i][index_root:])
                    else:
                        pass
                except:
                    pass
        
    return(eval("".join(list2)))

    #log(base)(ln(x)) Error 해결