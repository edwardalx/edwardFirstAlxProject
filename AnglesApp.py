Angle = float(input("What type of Angle is ... degrees?"))

if Angle < 90:
    print("Acute Angle")
if Angle == 90:
    print("Right-Angle")
if Angle < 180 and Angle > 90:
    print("Obtuse-Angle")
if Angle == 180:
    print("Straight Line")
if Angle < 360 and Angle > 180:
    print("Reflex-Angle")
if Angle == 360:
    print("Circle")
