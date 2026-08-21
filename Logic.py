condition = 5 > 0
if condition:
    print("Code A")
    print("Code A")
    print("Code A")

    print("Code B")

temp = 30
if temp > 25:
    print("It's really hot outside")


elif temp > 15:
    print("It's warm outside")


elif temp > 0:
    print("It's chill outside")


else:
    print("It's freezing cold")

x = 20
y = 40
if x > 0 and x < 100 and y < 100 and y > 0:
    print("xy Coordinate is good")

if x > 0:
    if x < 100:
        if y > 0:
            if y < 100:
                print("xy Coordinate is good")

panel_W = 900
panel_H = 2500

if panel_W <= 1500:
    print("Width is good.")

if panel_H <= 3000:
    print("Height is good.")

else:
    print("Height is not good.")
