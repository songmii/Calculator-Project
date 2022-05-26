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

     
def menu1(matA, matB, matC):  #1:Dim 행렬 A,B,C에 새로운 값을 줄 때 들어가는 메뉴
    matrix = ""
    while(True):
        matrix = input("Matrix?\n1.MatA 2.MatB 3.MatC\n") #A,B,C 중 선택
        print()
        if matrix == "1" or matrix == "2" or matrix == "3":
            break

    size = ""
    while(True):
        size = input("MatA (mxn)\n1.3x3 2.3x2 3.3x1 4.2x3 5.2x2 6.2x1\n")#선택된 행렬의 크기 선택
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

    if matrix == "1":
        print("A")
    elif matrix == "2":
        print("B")
    else:
        print("C")
    print(matrix_temp) #빈 행렬 print

    for i in range(len(matrix_temp)): #행렬을 [row][column]의 형식으로 입력 받아서 임시 저장
        for j in range(len(matrix_temp[i])):
            matrix_temp[i,j] = eval(input(f"[{i}][{j}] : ")) #eval 대신에 mode1 계산!!!!

    m = matrixs(matA, matB, matC)
    m.setMat(matrix, matrix_temp)
    matA, matB, matC = m.getMat()

    print() #지정한 행렬의 저장 결과 print
    if matrix == "1":
        print("A")
        print(matA)
    elif matrix == "2":
        print("B")
        print(matB)
    else:
        print("C")
        print(matC)
    print()

    return matA, matB, matC #행렬의 값 변경후 다시 return


def menu2(matA, matB, matC): #2:Data  행렬 A,B,C에 어떤 값이 저장되어있는지 확인하는 메뉴
    matrix = ""
    while(True):
        matrix = input("Matrix?\n1.MatA 2.MatB 3.MatC\n") #A,B,C 중 선택
        if matrix == "1" or matrix == "2" or matrix == "3":
            break

    if matrix == "1": #선택된 행렬을 print
        print("A")
        print(matA)
    elif matrix == "2":
        print("B")
        print(matB)
    else:
        print("C")
        print(matC)
    print()

   
def det(mat):#2x2 또는 3x3 행렬의 행렬식 계산

    if len(mat) == 0: #행렬에 저장된 값이 없는 경우
        print("Dimension Error")
        
    elif len(mat) != len(mat[0]): #행렬이 정사각행렬이 아닌 경우
        print("Dimension Error")
        
    if len(mat) == 2: #2x2
        return mat[0,0]*mat[1,1] - mat[0,1]*mat[1,0]
    
    else: #3x3
        return mat[0,0]*(mat[1,1]*mat[2,2]-mat[1,2]*mat[2,1])\
                -mat[0,1]*(mat[1,0]*mat[2,2]-mat[1,2]*mat[2,0])\
                +mat[0,2]*(mat[1,0]*mat[2,1]-mat[1,1]*mat[2,0])

    
def trn(mat): #행렬의 전치행렬 return
    if len(mat) == 0: #행렬에 저장된 값이 없는 경우
        print("Dimension Error")
    
    else:
        row = len(mat)
        column = len(mat[0])

        result = np.zeros((column,row), dtype = float)

        for i in range(column):
            for j in range(row):
                result[i, j] = mat[j, i]

        return result
    

def menu():
    menu = ""
    while(True):
        menu = input("1.Dim 2.Data 3.MatA 4.MatB 5.MatC 6.MatAns 7.det 8.Trn\n")
    
        if menu == "1" or menu == "2" or menu == "3" or menu == "4" or menu == "5" \
           or menu == "6" or menu == "7" or menu == "8":
            break
    return menu

            
def mode5(matA, matB, matC, eq):

    while(True):
        op = input("1:menu, 0:프로그램 종료\n")
        
        if op == "1":
            print()
            menu = ""
            menu = menu()
            
            if menu == "1":
                matA, matB, matC = menu1(matA, matB, matC)
            elif menu =="2":
                menu2(matA, matB, matC)
            elif menu =="3":
                equation += "MatA"
            elif menu =="4":
                equation += "MatB"
            elif menu =="5":
                equation += "MatC" #6 해야함!!!
            elif menu == "7":
                menu7(matA, matB, matC)
            elif menu == "8":
                menu8(matA, matB, matC)
            
        elif op == "0":
            print("===== 프로그램 종료 =====")
            break
        
        else:
            print("wrong input, try again.")
            print()
            

matA = []
matB = deepcopy(matA)
matC = deepcopy(matA)
eq = ""
mode5(matA, matB, matC, eq)
    



