# 1.
import math
import md1_func

def calc_mode1(s1): # s1 : 전체 입력 수식

    list1 = s1.split() # 수식을 띄어쓰기 단위로 나눈 list
    list2 = [] # eval이 되지 않는 부분을 모두 eval이 가능하도록 변경한 list

    for i in range(len(list1)):
        while(True):
            # print(list1[i])

            try:
                eval(list1[i]) #eval에 바로 통과가 되는 경우('int','float') 그대로 저장
                list2.append(list1[i])
                break

            except:  #eval에서 오류가 생기는 경우 => 함수 호출이 필요한 경우

                func_list= ["log", "ln", "sin", "cos", "tan", "asin", "acos", "atan", "sinh", "cosh", "tanh", "asinh", "acosh", "atanh", "pi", "e", "root"]
                func_dic = {}
                for j in range(len(func_list)):
                    func_dic[list1[i].rfind(func_list[j])] = func_list[j]
                
                rightmost = max(func_dic)
                func_rightmost = func_dic[rightmost]

                if func_rightmost == "log":
                    count_open = 0
                    count_close = 0
                    k = 0

                    while(True):
                        if list1[i][rightmost+3+k] == "(":
                            count_open +=1
                        if list1[i][rightmost+3+k] == ")":
                            count_close +=1
                        if count_open == count_close and count_open != 0:
                            break
                        k +=1
                    
                    base = eval(list1[i][rightmost+3:rightmost+3+k+1])

                    count_open = 0
                    count_close = 0
                    l = 0

                    while(True):
                        if list1[i][rightmost+3+k+1+l] == "(":
                            count_open +=1
                        if list1[i][rightmost+3+k+1+l] == ")":
                            count_close +=1
                        if count_open == count_close and count_open != 0:
                            break
                        l +=1
                    
                    value = eval(list1[i][rightmost+3+k+1:rightmost+3+k+1+l+1])
                    list1_temp = list1[i][:rightmost]+ str(math.log(value,base)) + list1[i][rightmost+3+k+1+l+1:] 
                    list1[i] = list1_temp


                
        return list2
            

#Test
#print(calc_mode1("log(2*4+log(2)(4))(5*log(3)(9))"))
