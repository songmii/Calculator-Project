import numpy as np
import random

def mat_inp(r, c): #matrix 사이즈 입력받고 matrix의 원소들 입력받아 matrix return
    mat = np.zeros((r,c))

    s = "   "
    for i in range(c):
        s += chr(ord("a") + i) + "   "
        
    print(s)
    for row in range(len(mat)):
        if row != 0:
            print()
        print("%d"%(row+1), end = " " )
        for col in range(len(mat[row])):
            print(mat[row,col], end = " ")
    print()

    for row in range(len(mat)):
        for col in range(len(mat[row])):
            while(True):
                try:
                    mat[row, col] = eval(input(f"[{row}, {col}] = "))
                    break
                except:
                    print("Try again\n")
                
            
    return mat


def menu1(mat): #2X3행렬 입력받아서 X,Y값을 "X = {X값}, Y = {Y값}"의 형태의  string으로 return
    '''
    2X3행렬 (Ax =b)
    a1x + b1y = c1
    a2x + b2y = c2
    '''
    if mat[0,0] == 0 and mat[0,1] ==0 and mat[0,2] != 0: # a1,b1 = 0이고 c1은 0이 아닌경우
        print("Math Error")
    elif mat[1,0] == 0 and mat[1,1] ==0 and mat[1,2] != 0: # a2,b2 = 0이고 c2은 0이 아닌경우
        print("Math Error")
    elif mat[0,0]*mat[1,1] == mat[1,0]*mat[0,1] and mat[0,2] != mat[1,2]: #a1*b2 = a2*b1 이지만 c1 != c2 인경우
        print("Math Error")        
    else:
        x = round((mat[0,2]*mat[1,1] - mat[1,2]*mat[0,1]) / (mat[0,0]*mat[1,1] - mat[1,0]*mat[0,1]),9)
        y = round((mat[0,2]*mat[1,0] - mat[1,2]*mat[0,0]) / (mat[1,0]*mat[0,1] - mat[0,0]*mat[1,1]),9)
        result = "X = {0}, Y = {1}".format(x,y)
        return result


def menu2(mat): #3X4행렬 입력받아서 X,Y값을 "X = {X값}, Y = {Y값}, Z = {Z값}"의 string으로 return
    '''
    3X4행렬 (Ax = b)
    a1x + b1y + c1z = d1
    a2x + b2y + c2z = d2
    a3x + b3y + c3z = d3
    '''
    mat_eq = np.zeros((3,3))
    mat_d = np.zeros((3,1))
    for i in range(3):
        mat_d[i] = mat[i,3]
        for j in range(3):
            mat_eq[i,j] = mat[i,j]


    mat_eq_inv = np.linalg.inv(mat_eq) 

    ans = np.dot(mat_eq_inv,mat_d) # x = (A 역행렬) * b
    
    result = f"X = {round(ans[0][0],9)}, Y = {round(ans[1][0],9)}, Z = {round(ans[2][0],9)}"
    return result


def menu3(mat): #3X1행렬 입력받아서 X,Y값을 "X1 = {X1값}, X2 = {X2값}"의 string으로 return
    '''
    3X1행렬
    ax^2 + bx + c = 0

    '''
    a = mat[0][0]
    b = mat[0][1]
    c = mat[0][2]
    result = ""

    if a == 0:
        print("Math Error")

    else:
        dis = b**2-4*a*c #판별식

        if dis == 0: # 중근
            x = -b/(2*a)
            result = f"X = {round(x,9)}"

        elif dis>0: # 서로 다른 두 실근
            x1 = (-b + dis**0.5)/(2*a)
            x2 = (-b - dis**0.5)/(2*a)
            result = f"X1 = {round(x1,9)}, X2 = {round(x2,9)}"

        else:# 서로 다른 두 허근
            real = round(-b/(2*a),9)
            imag = ((-dis)**0.5)/(2*a)
            imag = round(imag, 9)# 허수부 반올림
            x1 = real + imag*1j
            x2 = real - imag*1j
            result = f"X1 = {x1}, X2 = {x2}"

        return result
    

def func(a, b, c, d, x):#3차식의 계수와 x값을 입력받아 결과 return
    return (a * (x**3)) + (b * (x**2)) + (c * x) + d


def cubic(a,b,c,d):
    n = 2*(b**3)-9*a*b*c+27*(a**2)*d
    s = ((n**2 - (4*(b**2-3*a*c)**3)))**0.5
    r0 =  -(b/3/a)-(1/3/a)*(((n+s)/2)**(1/3)+((n-s)/2)**(1/3))
    r1 = -(b/3/a)+((1+(3**0.5)*1j)/6/a)*(((n+s)/2)**(1/3))+((1-(3**0.5)*1j)/6/a)*(((n-s)/2)**(1/3))
    r2 = -(b/3/a)+((1-(3**0.5)*1j)/6/a)*(((n+s)/2)**(1/3))+((1+(3**0.5)*1j)/6/a)*(((n-s)/2)**(1/3))
    return r0,r1,r2


def menu4(mat):#4X1행렬 입력받아서 X,Y값을 "X1 = {X1값}, X2 = {X2값}, X3 = {X3값}"의 string으로 return
    '''
    4X1행렬
    ax^3 + bx^2 + cx + d = 0

    '''
    a = float(mat[0][0])
    b = float(mat[0][1])
    c = float(mat[0][2])
    d = float(mat[0][3])

    if a == 0:
        print("Math Error")

    else:
        
        x1, x2, x3 = cubic(a,b,c,d)
        root = {x1, x2, x3}
        root_temp = list(root)

        result = ""
        for i in range(len(root)):
            x = "x" + f"{i+1}"
            x = eval(x)
            
            if isinstance(x,int) or isinstance(x,float):
                x = round(x,9)
                result = f"X{i+1} = " + f"{x}"
    
            elif isinstance(x, complex):
                real = x.real
                imag = x.imag
                real = round(real, 9)
                imag = round(imag, 9)
            
                result += f"X{i+1} = " + f"{real}"
                if imag != 0:
                    result += f"{imag}j"
                if i != len(root)-1:
                    result += ", "

        return result


def mode4(oname):
    ans = None
    ofile = open(oname, "a")

    while True:
        print('''
====================================
        연산 형식 입력 : (0 입력시 프로그램 종료)
        1. anX + bnY = cn
        2. anX + bnY + cnZ = dn
        3. aX2 + bX + c = 0
        4. aX3 + bX2 + cX + d = 0
        
        입력 예시
        연산 형식 >> 2
====================================
        ''')
        n = input("연산 형식>> ").strip()
        print()

        if n == '1':
            mat = mat_inp(2,3)
            ans = menu1(mat)
            if ans != None:
                ofile.write(str(mat) + "\n")
                ofile.write(ans + "\n\n")
                print(ans)


        elif n == '2':
            mat = mat_inp(3,4)
            ans = menu2(mat)
            if ans != None:
                ofile.write(str(mat) + "\n")
                ofile.write(ans + "\n\n")
                print(ans)

                
        elif n == '3':
            mat = mat_inp(1,3)
            ans = menu3(mat)
            if ans != None:
                ofile.write(str(mat) + "\n")
                ofile.write(ans + "\n\n")
                print(ans)
            

        elif n == '4':
            mat = mat_inp(1,4)
            ans = menu4(mat)
            if ans != None:
                ofile.write(str(mat) + "\n")
                ofile.write(ans + "\n\n")
                print(ans)


        elif n == '0':
            ofile.close()
            print('''
====================================
            프로그램 종료
====================================
            ''')
            exit(0)

        else:
            print("Invalid Input")
            



#mode4("output.txt")




