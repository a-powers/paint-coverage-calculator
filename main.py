import math

print("Welcome to the Paint Coverage Calculator.")
def paint_calc(height, width, cover):
    coverage = (height*width)/cover
    calc = math.ceil(coverage)
    print(f"You will need {calc} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(test_h,test_w,coverage)