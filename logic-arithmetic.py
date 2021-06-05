import cv2 as cv
import numpy as np

square = cv.imread('./img/square.png')
ball = cv.imread('./img/ball.png')

square_gray = cv.cvtColor(square, cv.COLOR_BGR2GRAY)
ball_gray = cv.cvtColor(ball, cv.COLOR_BGR2GRAY)


cv.imshow('Face recognized', image)
cv.waitKey(10000)
cv.destroyAllWindows()
