import math

def paint_calc(height, width, cover):
    coverage = (height*width)/cover
    calc = math.ceil(coverage)
    print(calc)


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)


