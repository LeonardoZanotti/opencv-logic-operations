# Logic and Arithmetic operations with OpenCV
Python and Opencv project to perform logic and arithmetic operations in images.

## Requirements
You will need [Python](https://www.python.org/) and [OpenCV](https://opencv.org/).

Linux already comes with a python version, is a bit old, so i recommend you to update it.
I have python3.7 here, so im using it.

First, lets install pip, a python package manager:
```bash
$ python3.7 -m pip install pip
```

Now, install OpenCV:
```bash
$ pip3.7 install opencv-contrib-python
```

Testing if the OpenCV is correctly installed:
```bash
$ python3.7     # will open the Python terminal
```
Import the OpenCV package and log the version of it:
```python
import cv2
cv2._version_
```
If no errors, we are done.

## Running the program
To run the program, just do:
```bash
$ python3.7 logic-arithmetic.py [arg1] [arg2]
```
Where `arg1` is a mandatory field, being one of the following values: `add`, `sub`, `mult`, `div`, `and`, `or`, `xor`, `not`, `blur`, `box`, `median`, `dd`, `gaussian` or `bilateral`, and `arg2` is an optional field, accepting only `special` as value, used to show a special view mode, comparing the original and the new image.

## References
MARQUES FILHO, Ogê; VIEIRA NETO, Hugo. Processamento Digital de Imagens, Rio de Janeiro: Brasport, 1999. ISBN 8574520098

[OpenCV Documentation](https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html)

## Leonardo Zanotti
