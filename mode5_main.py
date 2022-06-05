# mode 5 : MATRIX

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


def menu1(matA, matB, matC):  # 1:Dim 행렬 A,B,C에 새로운 값을 줄 때 들어가는 메뉴
    matrix = ""
    while (True):
        matrix = input("Matrix?\n1.MatA 2.MatB 3.MatC\n")  # A,B,C 중 선택
        print()
        if matrix == "1" or matrix == "2" or matrix == "3":
            break

    size = ""
    while (True):
        size = input("Mat (mxn)\n1.3x3 2.3x2 3.3x1 4.2x3 5.2x2 6.2x1\n")  # 선택된 행렬의 크기 선택
        print()
        if size == "1" or size == "2" or size == "3" or \
                size == "4" or size == "5" or size == "6":
            break

    matrix_temp = []
    if size == "1":
        matrix_temp = np.zeros((3, 3), dtype=float)
    elif size == "2":
        matrix_temp = np.zeros((3, 2), dtype=float)
    elif size == "3":
        matrix_temp = np.zeros((3, 1), dtype=float)
    elif size == "4":
        matrix_temp = np.zeros((2, 3), dtype=float)
    elif size == "5":
        matrix_temp = np.zeros((2, 2), dtype=float)
    else:
        matrix_temp = np.zeros((2, 1), dtype=float)

    while (True):
        input_type = input("Input type\n1.직접 식 입력\n2.파일 입력\n")
        print()
        if input_type == "1" or input_type == "2":
            break

    if input_type == "1":
        if matrix == "1":
            print("A")
        elif matrix == "2":
            print("B")
        else:
            print("C")
        print(matrix_temp)  # 빈 행렬 print
        for i in range(len(matrix_temp)):  # 행렬을 [row][column]의 형식으로 입력 받아서 임시 저장
            for j in range(len(matrix_temp[i])):
                while (True):
                    try:
                        while (True):
                            try:
                                matrix_temp[i, j] = eval(input(f"[{i}][{j}] : "))
                                break
                            except:
                                print("Try again\n")
                    except:
                        print("wrong input, try again.")
                    else:
                        break

    else:
        ifile = ""
        while (True):
            iname = input("Input File name : ")
            try:
                ifile = open(iname)
            except:
                print(f"{iname} does not exist")
            else:
                break

        element = []
        for line in ifile:
            line = line.strip()
            element += line.split()

        if len(matrix_temp) * len(matrix_temp[0]) != len(element):
            print("Input data does not match with selected matrix size")
        else:
            for i in range(len(element)):
                while (True):
                    try:
                        element[i] = eval(element[i])
                        break
                    except:
                        print("Try again\n")

            count = 0
            for i in range(len(matrix_temp)):
                for j in range(len(matrix_temp[i])):
                    matrix_temp[i, j] = element[count]
                    count += 1

    m = matrixs(matA, matB, matC)
    m.setMat(matrix, matrix_temp)
    matA, matB, matC = m.getMat()
    print()

    return matA, matB, matC  # 행렬의 값 변경후 다시 return


def menu2(matA, matB, matC):  # 2:Data  행렬 A,B,C에 어떤 값이 저장되어있는지 확인하는 메뉴
    matrix = ""
    while (True):
        matrix = input("Matrix?\n1.MatA 2.MatB 3.MatC\n")  # A,B,C 중 선택
        if matrix == "1" or matrix == "2" or matrix == "3":
            break

    if matrix == "1":  # 선택된 행렬을 print
        print("A")
        print(matA)
    elif matrix == "2":
        print("B")
        print(matB)
    else:
        print("C")
        print(matC)
    print()


def det(mat):  # 2x2 또는 3x3 행렬의 행렬식 계산

    if len(mat) == 0:  # 행렬에 저장된 값이 없는 경우
        print("Dimension Error")
        print()

    elif len(mat) != len(mat[0]):  # 행렬이 정사각행렬이 아닌 경우
        print("Dimension Error")
        print()

    if len(mat) == 2:  # 2x2
        return mat[0, 0] * mat[1, 1] - mat[0, 1] * mat[1, 0]

    else:  # 3x3
        return mat[0, 0] * (mat[1, 1] * mat[2, 2] - mat[1, 2] * mat[2, 1]) \
               - mat[0, 1] * (mat[1, 0] * mat[2, 2] - mat[1, 2] * mat[2, 0]) \
               + mat[0, 2] * (mat[1, 0] * mat[2, 1] - mat[1, 1] * mat[2, 0])


def trn(mat):  # 행렬의 전치행렬 return
    if len(mat) == 0:  # 행렬에 저장된 값이 없는 경우
        print("Dimension Error")
        print()

    else:
        row = len(mat)
        column = len(mat[0])

        result = np.zeros((column, row), dtype=float)

        for i in range(column):
            for j in range(row):
                result[i, j] = mat[j, i]

        return result


def dot(mat1, mat2):  # 9: martrix들의 dot product
    print(len(mat1[0]), len(mat2))
    if len(mat1) == 0 or len(mat2) == 0:
        print("wrong input, try again.")
        print()

    elif len(mat1[0]) == 0 or len(mat2[0]) == 0:
        print("wrong input, try again.")
        print()

    elif len(mat1[0]) != len(mat2):
        print("Dimension Error")
        print()

    else:
        return np.dot(mat1, mat2)


def menu_call():  # 메뉴 호출
    menu = ""
    while (True):
        menu = input("1.Dim 2.Data 3.MatA 4.MatB 5.MatC 6.MatAns 7.Det 8.Trn 9.Dot\n")

        if menu == "1" or menu == "2" or menu == "3" or menu == "4" or menu == "5" \
                or menu == "6" or menu == "7" or menu == "8" or menu == "9":
            break
    return menu


def calc_mode5(matA, matB, matC, matAns, s):
    # MatA,MatB,MatC,MatAns간의 +,-연산 또는 스칼라와의 연산 처리
    equation = ""
    if s == "MatA" or s == "MatB" or s == "MatC" or s == "MatAns":
        while (True):
            eq = input(f"식 입력('=' 입력시 결과 출력)\n{s}")
            s_temp = deepcopy(s)

            if eq[len(eq) - 1] == "=":
                s_temp += eq
                try:
                    eq_cal_final = s_temp[0:len(s_temp) - 1]
                    eq_cal_final = eq_cal_final.replace("MatAns", "matAns")
                    eq_cal_final = eq_cal_final.replace("MatA", "matA")
                    eq_cal_final = eq_cal_final.replace("MatB", "matB")
                    eq_cal_final = eq_cal_final.replace("MatC", "matC")
                    eval(eq_cal_final)
                except:
                    print("wrong input, try again.\n")
                else:
                    matAns = deepcopy(eval(eq_cal_final))
                    print(matAns)
                    print()
                    equation = s + eq
                    return equation, matAns
                    break
            else:
                print("wrong input, try again.\n")

    elif s == "det(":
        # 행렬 입력받아 식과 행렬식 결과 return
        while (True):
            eq = input(f"식 입력(')=' 입력시 결과 출력)\n{s}")
            s_temp = deepcopy(s)

            if eq[len(eq) - 2:len(eq)] == ")=":
                s_temp += eq
                try:
                    eq_cal_final = s_temp[4:-2]
                    eq_cal_final = eq_cal_final.replace("MatAns", "matAns")
                    eq_cal_final = eq_cal_final.replace("MatA", "matA")
                    eq_cal_final = eq_cal_final.replace("MatB", "matB")
                    eq_cal_final = eq_cal_final.replace("MatC", "matC")
                    eval(eq_cal_final)
                except:
                    print("wrong input, try again.\n")
                else:
                    print(det(eval(eq_cal_final)))
                    print()
                    equation = s + eq
                    return equation, det(eval(eq_cal_final))
                    break
            else:
                print("wrong input, try again.\n")

    elif s == "trn(":
        # 행렬 입력받아 식과 전치행렬 return
        while (True):
            eq = input(f"식 입력(')=' 입력시 결과 출력)\n{s}")
            s_temp = deepcopy(s)

            if eq[len(eq) - 2:len(eq)] == ")=":
                s_temp += eq
                try:
                    eq_cal_final = s_temp[4:-2]
                    eq_cal_final = eq_cal_final.replace("MatAns", "matAns")
                    eq_cal_final = eq_cal_final.replace("MatA", "matA")
                    eq_cal_final = eq_cal_final.replace("MatB", "matB")
                    eq_cal_final = eq_cal_final.replace("MatC", "matC")
                    eval(eq_cal_final)
                except:
                    print("wrong input, try again.\n")
                else:
                    matAns = trn(eval(eq_cal_final))
                    print(matAns)
                    print()
                    equation = s + eq
                    return equation, trn(eval(eq_cal_final))
                    break
            else:
                print("wrong input, try again.\n")


def mode5(oname):
    matA = []
    matB = deepcopy(matA)
    matC = deepcopy(matA)
    matAns = deepcopy(matA)
    ofile = open(oname, "a")

    while (True):
        op = input("0:프로그램 종료, 1:menu\n")

        if op == "1":
            print()
            menu = ""
            menu = menu_call()
            eq_cal = ""

            if menu == "1":
                matA, matB, matC = menu1(matA, matB, matC)

            elif menu == "2":
                menu2(matA, matB, matC)

            elif menu == "3":
                try:
                    equation, matAns = calc_mode5(matA, matB, matC, matAns, "MatA")
                    ans = str(matAns)
                    ofile.write(equation + "\n")
                    ofile.write(ans + "\n\n")

                except:
                    pass

            elif menu == "4":
                try:
                    equation, matAns = calc_mode5(matA, matB, matC, matAns, "MatB")
                    ans = str(matAns)
                    ofile.write(equation + "\n")
                    ofile.write(ans + "\n")
                except:
                    pass

            elif menu == "5":
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
                    equation, ans_temp = calc_mode5(matA, matB, matC, matAns, "trn(")
                    ans = str(ans_temp)
                    ofile.write(equation + "\n")
                    ofile.write(ans + "\n\n")
                except:
                    pass

            elif menu == "9":
                # MatA,MatB,MatC,MatAns중에 두개의 dot product만 지원
                # X*Y의 형태
                eq = "(  )*(  )"
                print(eq)
                matrix1 = ""
                while (True):
                    matrix1 = input("Matrix?\n1.MatA 2.MatB 3.MatC 4.MatAns\n")  # X matrix
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
                while (True):
                    matrix2 = input("Matrix?\n1.MatA 2.MatB 3.MatC 4.MatAns\n")  # Y matrix
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
                matAns = dot(eval(eq_dot[0]), eval(eq_dot[1]))
                print(matAns)
                print()
                ans = str(matAns)
                ofile.write(equation + "\n")
                ofile.write(ans + "\n\n")


        elif op == "0":
            print("===== 프로그램 종료 =====")
            ofile.close()
            break

        else:
            print("wrong input, try again.")
            print()

# mode5("output.txt")



