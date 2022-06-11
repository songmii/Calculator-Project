#mode 5 : MATRIX

import numpy as np
from copy import deepcopy
from math import *

class matrixs():

    def __init__(self, matA, matB, matC):
        self.matA = matA
        self.matB = matB
        self.matC = matC

    def setMat(self, matrix, matrix_temp):
        if matrix == "1":
            self.matA = deepcopy(matrix_temp)
        elif matrix == "2":
            self.matB = deepcopy(matrix_temp)
        else:
            self.matC = deepcopy(matrix_temp)

    def getMat(self):
        return self.matA, self.matB, self.matC

     
def menu1(matA, matB, matC):  #1:Dim 행렬 A,B,C에 새로운 값을 입력할 때 들어가는 메뉴
    matrix = ""
    while(True):
        matrix = input('''
=================================
    행렬 선택
    1.MatA
    2.MatB
    3.MatC
=================================
>> ''') #A,B,C 중 선택
        if matrix == "1" or matrix == "2" or matrix == "3":
            break

    size = ""
    while(True):
        size = input('''
=================================
    행렬 크기 (mxn)
    1.3x3
    2.3x2
    3.3x1
    4.2x3
    5.2x2
    6.2x1
=================================
>> ''')#선택된 행렬의 크기 선택
        print()
        if size == "1" or size == "2" or size == "3" or \
           size == "4" or size == "5" or size == "6":
            break
        
    matrix_temp = []
    if size == "1":
        matrix_temp = np.zeros((3,3), dtype = float)
    elif size == "2":
        matrix_temp = np.zeros((3,2), dtype = float)
    elif size == "3":
        matrix_temp = np.zeros((3,1), dtype = float)
    elif size == "4":
        matrix_temp = np.zeros((2,3), dtype = float)
    elif size == "5":
        matrix_temp = np.zeros((2,2), dtype = float)
    else:
        matrix_temp = np.zeros((2,1), dtype = float)

    while (True):
        input_type = input('''
=================================
    입력 형식
    1. 식 입력
    2. 파일 입력
=================================
입력 형식>> ''')

        if input_type == "1" or input_type == "2":
            break
        
        else:
            print("잘못된 입력\n")
    
    if input_type == "1":
        if matrix == "1":
            print("A")
        elif matrix == "2":
            print("B")
        else:
            print("C")
        print(matrix_temp) #빈 행렬 print
        for i in range(len(matrix_temp)): #행렬을 [row][column]의 형식으로 입력 받아서 임시 저장
            for j in range(len(matrix_temp[i])):
                while(True):
                    try:
                        while(True):
                            try:
                                matrix_temp[i,j] = eval(input(f"[{i}][{j}] : "))
                                break
                            except:
                                print("잘못된 입력\n")
                    except:
                        print("잘못된 입력\n")
                    else:
                        break
                    
        m = matrixs(matA, matB, matC)
        m.setMat(matrix, matrix_temp)
        matA, matB, matC = m.getMat()
        print()
        
    else:
        print("""
==============================================================
    파일 입력 모드
    
    입력의 개수가 선택한 행렬 크기에 맞게 작성되어야 합니다
    형식 숫자 또는 식을 입력하고 띄어쓰기로 각각을 구분합니다


    파일 형식 예시
    
    input.txt
    1 2 -4 2 0 5
    
    input.txt
    1.0 2.4 -3.2 5.89
    4.2 1+3 3*5
    9
==============================================================
""")
        ifile = ""
        while (True):
            iname = input("파일 이름>> ")
            try : 
                ifile = open(iname)
            except:
                print("존재하지 않는 파일입니다.")
            else:
                break

        element = []
        for line in ifile:
            line = line.strip()
            element += line.split()

        if len(matrix_temp)*len(matrix_temp[0]) != len(element):
            print("입력의 개수가 선택한 행렬 크기에 맞지 않습니다")
            
        else:
            for i in range(len(element)):
                while(True):
                    try:
                        element[i] = eval(element[i])
                        break
                    except:
                       print("잘못된 입력\n")
                
            count = 0
            for i in range(len(matrix_temp)):
                for j in range(len(matrix_temp[i])):
                    matrix_temp[i,j] = element[count]
                    count +=1
                  
            m = matrixs(matA, matB, matC)
            m.setMat(matrix, matrix_temp)
            matA, matB, matC = m.getMat()
            print()

    return matA, matB, matC #행렬의 값 변경후 다시 return


def menu2(matA, matB, matC): #2:Data  행렬 A,B,C에 어떤 값이 저장되어있는지 확인하는 메뉴
    matrix = ""
    while(True):
        matrix = input('''
=================================
    행렬 선택
    1.MatA
    2.MatB
    3.MatC
=================================
>> ''') #A,B,C 중 선택
        if matrix == "1" or matrix == "2" or matrix == "3":
            break

    if matrix == "1": #선택된 행렬을 print
        if len(matA) != 0:
            print("A")
            print(matA)
        else:
            print("입력된 값이 없습니다.")
            
    elif matrix == "2":
        if len(matB) != 0:
            print("B")
            print(matB)
        else:
            print("입력된 값이 없습니다.")
            
    else:
        if len(matC) != 0:
            print("C")
            print(matC)
        else:
            print("입력된 값이 없습니다.")
            
    print()

   
def det(mat):#2x2 또는 3x3 행렬의 행렬식 계산

    if len(mat) == 0: #행렬에 저장된 값이 없는 경우
        print("Dimension Error")
        print()
        
    elif len(mat) != len(mat[0]): #행렬이 정사각행렬이 아닌 경우
        print("Dimension Error")
        print()
        
    if len(mat) == 2: #2x2
        return round(mat[0,0]*mat[1,1] - mat[0,1]*mat[1,0],9)
    
    else: #3x3
        return round(mat[0,0]*(mat[1,1]*mat[2,2]-mat[1,2]*mat[2,1])\
                -mat[0,1]*(mat[1,0]*mat[2,2]-mat[1,2]*mat[2,0])\
                +mat[0,2]*(mat[1,0]*mat[2,1]-mat[1,1]*mat[2,0]),9)

    
def trn(mat): #행렬의 전치행렬 return
    if len(mat) == 0: #행렬에 저장된 값이 없는 경우
        print("Dimension Error")
        print()        
    
    else:
        row = len(mat)
        column = len(mat[0])

        result = np.zeros((column,row), dtype = float)

        for i in range(column):
            for j in range(row):
                result[i, j] = mat[j, i]

        return result


def mul(mat1, mat2): #9: martrix의 곱 연산
    
    if len(mat1) ==0 or len(mat2) ==0:
        print("잘못된 입력\n")

    elif len(mat1[0]) ==0 or len(mat2[0]) ==0:
        print("잘못된 입력\n")
        
    elif len(mat1[0]) != len(mat2):
        print("Dimension Error")
        print()

    else:
        return np.matmul(mat1, mat2)
    
    

def menu_call():# 메뉴 호출
    menu = ""
    while(True):
        menu = input('''
==============================================================
        메뉴 입력 : (0 입력시 프로그램 종료)
        1. Dim : 행렬에 값을 입력합니다
        2. Data : 행렬에 입력된 값을 확인합니다
        3. MatA : 행렬A를 이용한 연산을 합니다
        4. MatB : 행렬B를 이용한 연산을 합니다
        5. MatC : 행렬C를 이용한 연산을 합니다
        6. MatAns : 직전 결과값인 행렬을 이용한 연산을 합니다
        7. Det : 행렬의 행렬식을 계산합니다
        8. Trn : 행렬의 전치행렬을 계산합니다
        9. Mul : 행렬들의 곱을 계산합니다

        0을 입력할 시 프로그램 종료
    
        입력 예시
        >> 1
==============================================================
연산 형식>> ''')
    
        if menu == "1" or menu == "2" or menu == "3" or menu == "4" or menu == "5" \
           or menu == "6" or menu == "7" or menu == "8" or menu == "9" or menu == "0":
            break
    return menu


def calc_mode5(matA, matB, matC, matAns, s):
    #MatA,MatB,MatC,MatAns간의 +,-연산 또는 스칼라와의 연산 처리
    equation = ""
    if s == "MatA" or s == "MatB" or s == "MatC" or s == "MatAns":
        while(True):
            eq = input('''
==============================================================
    식 입력 : '=' 입력시 결과 출력

    행렬간의 +,-,
    행렬과 스칼라의 *,/을 지원합니다

    행렬간의 곱셈의 경우
    => 연산 형식 입력 => 9.Mul 

    입력 예시
    >> = 
    >> + MatAns =
    >> -MatA+(MatB+MatC)= 
==============================================================
>> ''' + f"{s}")
            s_temp = deepcopy(s)

            if eq[len(eq)-1] == "=":
                s_temp += eq 
                try:
                    eq_cal_final = s_temp[0:len(s_temp)-1]
                    eq_cal_final = eq_cal_final.replace("MatAns", "matAns")
                    eq_cal_final = eq_cal_final.replace("MatA", "matA")
                    eq_cal_final = eq_cal_final.replace("MatB", "matB")
                    eq_cal_final = eq_cal_final.replace("MatC", "matC")
                    eval(eq_cal_final)
                except:
                    print("잘못된 입력\n")
                else:
                    matAns = deepcopy(eval(eq_cal_final))
                    print(matAns)
                    print()
                    equation = s + eq
                    return equation, matAns
                    break
            else:
                print("잘못된 입력\n")
                
    elif s == "det(":
        #행렬 입력받아 식과 행렬식 결과 return
        while(True):
            eq = input('''
==============================================================
    식 입력 : ')=' 입력시 결과 출력

    괄호 안의 행렬의 행렬식을 계산합니다

    입력 예시
    >> MatA)= 
    >> MatB + MatC*2)=
    >> -MatA+(MatB+MatC) )= 
==============================================================
>>''' + f"{s}")
            s_temp = deepcopy(s)

            if eq[len(eq)-2:len(eq)] == ")=":
                s_temp += eq 
                try:
                    eq_cal_final = s_temp[4:-2]
                    eq_cal_final = eq_cal_final.replace("MatAns", "matAns")
                    eq_cal_final = eq_cal_final.replace("MatA", "matA")
                    eq_cal_final = eq_cal_final.replace("MatB", "matB")
                    eq_cal_final = eq_cal_final.replace("MatC", "matC")
                    eval(eq_cal_final)
                except:
                    print("잘못된 입력\n")
                else:
                    print(det(eval(eq_cal_final)))
                    print()
                    equation = s + eq
                    return equation, det(eval(eq_cal_final))
                    break
            else:
                print("잘못된 입력\n")

    elif s == "trn(":
        #행렬 입력받아 식과 전치행렬 return
        while(True):
            eq = input('''
==============================================================
    식 입력 : ')=' 입력시 결과 출력

    괄호 안의 행렬의 전치 행렬을 계산합니다

    입력 예시
    >> MatA)= 
    >> MatB + MatC*2)=
    >> -MatA+(MatB+MatC) )= 
==============================================================
>> ''' + f"{s}")
            s_temp = deepcopy(s)

            if eq[len(eq)-2:len(eq)] == ")=":
                s_temp += eq 
                try:
                    eq_cal_final = s_temp[4:-2]
                    eq_cal_final = eq_cal_final.replace("MatAns", "matAns")
                    eq_cal_final = eq_cal_final.replace("MatA", "matA")
                    eq_cal_final = eq_cal_final.replace("MatB", "matB")
                    eq_cal_final = eq_cal_final.replace("MatC", "matC")
                    eval(eq_cal_final)
                except:
                    print("잘못된 입력\n")
                else:
                    matAns = trn(eval(eq_cal_final))
                    print(matAns)
                    print()
                    equation = s + eq
                    return equation, trn(eval(eq_cal_final))
                    break
            else:
                print("잘못된 입력\n")


def mode5(oname):
    matA = []
    matB = deepcopy(matA)
    matC = deepcopy(matA)
    matAns = deepcopy(matA)
    ofile = open(oname, "a")

    while(True):
        
        menu = ""
        menu = menu_call()
        eq_cal = ""

            
        if menu == "1":
            matA, matB, matC = menu1(matA, matB, matC)
            
        elif menu =="2":
             menu2(matA, matB, matC)
                
        elif menu =="3":
            try:
                equation, matAns = calc_mode5(matA, matB, matC, matAns, "MatA")
                ans = str(matAns)
                ofile.write(equation + "\n")
                ofile.write(ans + "\n\n")
            
            except:
                pass
                        
        elif menu =="4":
            try:
                equation, matAns = calc_mode5(matA, matB, matC, matAns, "MatB")
                ans = str(matAns)
                ofile.write(equation + "\n")
                ofile.write(ans + "\n")
            except:
                pass

        elif menu =="5":
            try:
                equation, matAns = calc_mode5(matA, matB, matC, matAns, "MatC")
                ans = str(matAns)
                ofile.write(equation + "\n")
                ofile.write(ans + "\n\n")
            except:
                pass
                        
        elif menu == "6":
            try:
                equation, matAns = calc_mode5(matA, matB, matC, matAns, "MatAns")
                ans = str(matAns)
                ofile.write(equation + "\n")
                ofile.write(ans + "\n\n")
            except:
                pass
                        
        elif menu == "7":
            try:
                equation, ans_temp = calc_mode5(matA, matB, matC, matAns, "det(")
                ans = str(ans_temp)
                ofile.write(equation + "\n")
                ofile.write(ans + "\n\n")
            except:
                pass
                        
        elif menu == "8":
            try:
                equation, matAns = calc_mode5(matA, matB, matC, matAns, "trn(")
                ans = str(ans_temp)
                ofile.write(equation + "\n")
                ofile.write(ans + "\n\n")
            except:
                pass
                        
        elif menu == "9":
            #MatA,MatB,MatC,MatAns중에 두개의 dot product만 지원
            #X*Y의 형태
            eq = "(  )*(  )"
            print(eq)
            matrix1 = ""
            while(True):
                matrix1 = input('''
=================================
    행렬 선택
    1.MatA
    2.MatB
    3.MatC
    4.MatAns
=================================
>> ''') #X matrix
                if matrix1 == "1" or matrix1 == "2" or matrix1 == "3" or matrix1 == "4":
                    break
            if matrix1 == "1":
                eq = "MatA*"
                print(eq)
            elif matrix1 == "2":
                eq = "MatB*"
                print(eq)
            elif matrix1 == "3":
                eq = "MatC*"
                print(eq)
            elif matrix1 == "4":
                eq = "MatAns*"
                print(eq)
            matrix2 = ""
            while(True):
                matrix2 = input('''
=================================
    행렬 선택
    1.MatA
    2.MatB
    3.MatC
    4.MatAns
=================================
>> ''') #Y matrix
                if matrix2 == "1" or matrix2 == "2" or matrix2 == "3" or matrix2 == "4":
                    break
            eq1 = ""
            if matrix2 == "1":
                eq1 = "MatA"
            elif matrix2 == "2":
                eq1 = "MatB"
            elif matrix2 == "3":
                eq1 = "MatC"
            elif matrix2 == "4":
                eq1 = "MatAns"

            eq_final = eq + eq1
            print(eq_final)
            equation = eq_final

            eq_final = eq_final.replace("MatAns", "matAns")
            eq_final = eq_final.replace("MatA", "matA")
            eq_final = eq_final.replace("MatB", "matB")
            eq_final = eq_final.replace("MatC", "matC")

            eq_dot = eq_final.split("*")
            matAns = mul(eval(eq_dot[0]), eval(eq_dot[1]))
            print(matAns)
            print()
            ans = str(matAns)
            ofile.write(equation + "\n")
            ofile.write(ans + "\n\n")
        

        elif menu == "0":
            print("""
==============================================================
                        프로그램 종료
==============================================================
""")
            ofile.close()
            break
        
        else:
            print("잘못된 입력\n")


            
mode5("output.txt")
            


