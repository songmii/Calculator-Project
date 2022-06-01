import numpy as np
import random

def mat_inp(r, c):
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
            mat[row, col] = eval(input(f"[{row}, {col}] = ")) #eval => mode1
            
    return mat


def menu1(mat):
    if mat[0,0] == 0 and mat[0,1] ==0 and mat[0,2] != 0:
        print("Math Error")
    elif mat[1,0] == 0 and mat[1,1] ==0 and mat[1,2] != 0:
        print("Math Error")
    elif mat[0,0]*mat[1,1] == mat[1,0]*mat[0,1] and mat[0,2] != mat[1,2]:
        print("Math Error")        
    else:
        x = round((mat[0,2]*mat[1,1] - mat[1,2]*mat[0,1]) / (mat[0,0]*mat[1,1] - mat[1,0]*mat[0,1]),9)
        y = round((mat[0,2]*mat[1,0] - mat[1,2]*mat[0,0]) / (mat[1,0]*mat[0,1] - mat[0,0]*mat[1,1]),9)
        result = "X = {0}, Y = {1}".format(x,y)
        return result


def menu2(mat):
    mat_eq = np.zeros((3,3))
    mat_d = np.zeros((3,1))
    for i in range(3):
        mat_d[i] = mat[i,3]
        for j in range(3):
            mat_eq[i,j] = mat[i,j]


    mat_eq_inv = np.linalg.inv(mat_eq)

    ans = np.dot(mat_eq_inv,mat_d)
    
    print(ans)
    result = f"X = {round(ans[0][0],9)}, Y = {round(ans[1][0],9)}, Z = {round(ans[2][0],9)}"
    return result


def menu3(mat):
    a = mat[0][0]
    b = mat[0][1]
    c = mat[0][2]
    result = ""

    if a == 0:
        print("Math Error")

    else:
        dis = b**2-4*a*c

        if dis == 0:
            x = -b/(2*a)
            result = f"X = {round(x,9)}"

        elif dis>0:
            x1 = (-b + dis**0.5)/(2*a)
            x2 = (-b - dis**0.5)/(2*a)
            result = f"X1 = {round(x1,9)}, X2 = {round(x2,9)}"

        else:
            real = round(-b/(2*a),9)
            imag = ((-dis)**0.5)/(2*a)
            imag = round(imag, 9)
            x1 = real + imag*1j
            x2 = real - imag*1j
            result = f"X1 = {x1}, X2 = {x2}"

        return result
    

def func(a, b, c, d, x):
    return (a * (x**3)) + (b * (x**2)) + (c * x) + d


def cubic(a,b,c,d):
    n = -b**3/27/a**3 + b*c/6/a**2 - d/2/a
    s = (n**2 + (c/3/a - b**2/9/a**2)**3)**0.5
    r0 = (n-s)**(1/3)+(n+s)**(1/3) - b/3/a
    r1 = (n+s)**(1/3)+(n+s)**(1/3) - b/3/a
    r2 = (n-s)**(1/3)+(n-s)**(1/3) - b/3/a
    return (r0,r1,r2)


def menu4(mat):
    a = mat[0][0]
    b = mat[0][1]
    c = mat[0][2]
    d = mat[0][3]

    if a == 0:
        print("Math Error")

    else:
        '''
        x1, x2, x3 = cubic(a,b,c,d)
        root = {x1, x2, x3}
        root_temp = list(root)

        result = ""
        for i in range(len(root)):
            x = "x" + f"{i+1}"
            result += f"X{i+1} = " + str(round(root_temp[i],9))
            if i != len(root)-1:
                result += ", "
        '''

        p = 0
        q = 0
        while(True):
            r1 = random.randint(-100,100)
            r2 = random.randint(-100,100)

            if func(a, b, c, d, r1)*func(a, b, c, d, r2) <0:
                p, q = r1, r2
                break

        m = (p+q)/2
        error = abs(func(a,b,c,d,m))

        while error != 0:
            if func(a,b,c,d,m)*func(a,b,c,d,p) < 0:
                q = m
            else:
                p = m
            m_temp = m
            m = (p+q)/2
            if m_temp == m:
                break
            error = abs(func(a,b,c,d,m))

        x1 = 0

        if (round(m) == round(m,2) and round(m) == round(m,3) and round(m) == round(m,4) and round(m) == round(m,5)):
            x1 = round(m, 4)
        else:
            x1 = round(m, 9)

        
        b, c = b+a*x1, c+(b+a*x1)*x1
        dis = (b**2)-4*a*c

        if dis == 0:
            x2 = -b/(2*a)
            if (round(x2) == round(x2,2) and round(x2) == round(x2,3) and round(x2) == round(x2,4) and round(x2) == round(x2,5)):
                x2 = round(x2, 4)
                e
            else:
                x2 = round(x2, 9)
            if x1 == x2:
                result = f"X = {x1}"
            else :
                result = f"X1 = {x1}, X2 = {round(x2,9)}"
                

        elif dis>0:
            x2 = (-b + dis**0.5)/(2*a)
            x3 = (-b - dis**0.5)/(2*a)
            if (round(x2) == round(x2,2) and round(x2) == round(x2,3) and round(x2) == round(x2,4) and round(x2) == round(x2,5)):
                x2 = round(x2, 4)
            else:
                x2 = round(x2, 9)
            if (round(x3) == round(x3,2) and round(x3) == round(x3,3) and round(x3) == round(x3,4) and round(x3) == round(x3,5)):
                x3 = round(x3, 4)
            else:
                x3 = round(x3, 9)
            if x1 == x2:
                result = f"X1 = {x1}, X2 = {round(x3,9)}"
            elif x1 == x3:
                result = f"X1 = {x1}, X2 = {round(x2,9)}"
            else:
                result = f"X1 = {x1}, X2 = {round(x2,9)}, X3 = {round(x3,9)}"

        else:
            real = -b/(2*a)
            if (round(real) == round(real,2) and round(real) == round(real,3) and round(real) == round(real,4) and round(real) == round(real,5)):
                real = round(real, 4)
            else:
                real = round(real, 9)

            imag = ((-dis)**0.5)/(2*a)
            if (round(imag) == round(imag,2) and round(imag) == round(imag,3) and round(imag) == round(imag,4) and round(imag) == round(imag,5)):
                imag = round(imag, 4)
            else:
                imag = round(imag, 9)
            x2 = real + imag*1j
            x3 = real - imag*1j
            result = f"X1 = {x1}, X2 = {x2}, X3 = {x3}"
    


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
            


mode4("output.txt")







