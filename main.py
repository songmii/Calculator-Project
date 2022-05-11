def calc_mode1(s1): # s1 : 전체 수식
    try:
        result = eval(s1) # s1이 eval만으로 계산가능할 경우

    except:
        list1 = s1.split() # 수식을 띄어쓰기 단위로 나눠서 list에
        list2 = []*len(list1) # eval이 되지 않는 부분을 모두 정리한후의 list

        for i in range(len(list1)):
            index_log = list1[i].find("log") #index_log : "log"가 존재하는 index, 없으면 -1 return
            if (index_log != -1):
                list2[i] = list1[i][0:index_log] + log(list1[i][index_log:])

            index_ln = list1[i].find("ln")
            if (index_ln != -1):
                list2[i] = list1[i][0: index_ln] + ln(list1[i][index_ln:])

            index_sin = list1[i].find("sin")
            if (index_sin != -1):
                list2[i] = list1[i][0: index_sin] + sin(list1[i][index_sin:])

            index_cos = list1[i].find("cos")
            if (index_cos != -1):
                list2[i] = list1[i][0: index_cos] + cos(list1[i][index_cos:])

            index_tan = list1[i].find("tan")
            if (index_tan != -1):
                list2[i] = list1[i][0: index_tan] + tan(list1[i][index_tan:])

            index_sin = list1[i].find("sin")
            if (index_sin != -1):
                list2[i] = list1[i][0: index_sin] + ln(list1[i][index_sin:])

            index_cos = list1[i].find("cos")
            if (index_cos != -1):
                list2[i] = list1[i][0: index_cos] + ln(list1[i][index_cos:])

            index_tan = list1[i].find("tan")
            if ( index_tan != -1):
                list2[i] = list1[i][0: index_tan] + ln(list1[i][index_tan:])




