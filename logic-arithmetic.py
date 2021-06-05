import cv2 as cv
import numpy as np
import sys
from matplotlib import pyplot as plt

def main():
    square = cv.imread('./img/square.png')
    ball = cv.imread('./img/ball.png')
    mask = cv.imread('./img/mask2.png')

    square_gray = cv.cvtColor(square, cv.COLOR_BGR2GRAY)
    ball_gray = cv.cvtColor(ball, cv.COLOR_BGR2GRAY)

    args = sys.argv
    if (len(args) > 1):
        if (args[1] == 'add'):
            title = 'Addition'
            image = add(square, ball)
        elif (args[1] == 'sub'):
            title = 'Subtraction'
            image = sub(square, ball)
        elif (args[1] == 'mult'):
            title = 'Multiplication'
            image = mult(square, ball)
        elif (args[1] == 'div'):
            title = 'Division'
            image = div(square, ball)
        elif (args[1] == 'and'):
            title = 'And operation'
            image = andF(square, ball)
        elif (args[1] == 'or'):
            title = 'Or operation'
            image = orF(square, ball)
        elif (args[1] == 'xor'):
            title = 'Xor operation'
            image = xorF(square, ball)
        elif (args[1] == 'not'):
            title = 'Not operation'
            image = notF(square, ball)
        elif (args[1] == 'blur'):
            title = 'Blur'
            image = blur(mask)
        elif (args[1] == 'box'):
            title = 'Box filter'
            image = box(mask)
        elif (args[1] == 'median'):
            title = 'Median filter'
            image = median(mask)
        elif (args[1] == 'dd'):
            title = '2D filter'
            image = dd(mask)
        elif (args[1] == 'gaussian'):
            title = 'Gaussian filter'
            image = gaussian(mask)
        elif (args[1] == 'bilateral'):
            title = 'Bilateral filter'
            image = bilateral(mask)
        else:
            print('(!) -- Error - no operation called')
            exit(0)

        if (len(args) > 2 and args[2] == 'special'):
            original = mask if args[1] == 'blur' or args[1] == 'box' or args[1] == 'median' or args[1] == 'dd' or args[1] == 'gaussian' or args[1] == 'bilateral' else square
            plt.subplot(121),plt.imshow(original),plt.title('Original')
            plt.xticks([]), plt.yticks([])
            plt.subplot(122),plt.imshow(image),plt.title(title)
            plt.xticks([]), plt.yticks([])
            plt.show()
        else:
            cv.imshow(title, image)
            cv.waitKey(15000)
            cv.destroyAllWindows()
    else:
        print('(!) -- Error - no operation called')
        exit(0)

def add(image1, image2):
    # return cv.add(image1, image2, 0)
    return cv.addWeighted(image1, 0.7, image2, 0.3, 0)

def sub(image1, image2):
    return cv.subtract(image1, image2, 0)

def mult(image1, image2):
    return cv.multiply(image1, image2)

def div(image1, image2):
    return cv.divide(image1, image2)

def andF(image1, image2):
    return cv.bitwise_and(image1, image2)

def orF(image1, image2):
    return cv.bitwise_or(image1, image2)

def xorF(image1, image2):
    return cv.bitwise_xor(image1, image2)

def notF(image1, image2):
    return cv.bitwise_not(image1)

def blur(image1):
    return cv.blur(image1, (5, 5))

def box(image1):
    return cv.boxFilter(image1, 50, (5, 5), False)

def median(image1):
    return cv.medianBlur(image1, 5)

def dd(image1):
    kernel = np.ones((5,5),np.float32)/25
    return cv.filter2D(image1, -1, kernel)

def gaussian(image1):
    return cv.GaussianBlur(image1, (5, 5), 0)

def bilateral(image1):
    return cv.bilateralFilter(image1, 9, 75, 75)

if __name__ == '__main__':
    main()
