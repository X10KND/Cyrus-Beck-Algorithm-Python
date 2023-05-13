SHOW_CALCULATION = False

def showcalc(*arg):
    if SHOW_CALCULATION:
        for a in arg:
            print(a, end="  ")
        print("\n")

def CyrusClipping(x0, y0, x1, y1):

    dx = x1 - x0
    dy = y1 - y0

    if dx != 0:
        t_left = -(x0 - x_min) / (x1 - x0)
        t_right = -(x0 - x_max) / (x1 - x0)
        showcalc("Left:", t_left, "Right:", t_right)

    if dy != 0:
        t_top = -(y0 - y_max) / (y1 - y0)
        t_bottom = -(y0 - y_min) / (y1 - y0)
        showcalc("Top:", t_top, "Bottom:", t_bottom)

    tE = 0
    tL = 1

    showcalc("Dx:", dx, "Dy:", dy)


    if dx == 0:
        if x0 < x_min or x0 > x_max:
            print("Line Completely outside")
            return

    elif dx < 0:
        tE = max(tE, t_right)
        showcalc("Right Edge\n", "Ni.D", dx, "PE", "tE:", tE, "tL:", tL)
        tL = min(tL, t_left)
        showcalc("Left Edge\n", "Ni.D", -dx, "PE", "tE:", tE, "tL:", tL)

    elif dx > 0:
        tE = max(tE, t_left)
        showcalc("Left Edge\n", "Ni.D", -dx, "PL", "tE:", tE, "tL:", tL)
        tL = min(tL, t_right)
        showcalc("Right Edge\n", "Ni.D", dx, "PL", "tE:", tE, "tL:", tL)

    if dy == 0:
        if y0 < y_min or y0 > y_max:
            print("Line Completely outside")
            return

    elif dy < 0:
        tE = max(tE, t_top)
        showcalc("Top Edge\n", "Ni.D", dy, "PE", "tE:", tE, "tL:", tL)
        tL = min(tL, t_bottom)
        showcalc("Bottom Edge\n", "Ni.D", -dy, "PE", "tE:", tE, "tL:", tL)

    elif dy > 0:
        tE = max(tE, t_bottom)
        showcalc("Bottom Edge\n", "Ni.D", -dy, "PL", "tE:", tE, "tL:", tL)
        tL = min(tL, t_top)
        showcalc("Top Edge\n", "Ni.D", dy, "PL", "tE:", tE, "tL:", tL)

    if tE < tL:
        xc1 = x0 + tE * dx
        yc1 = y0 + tE * dy

        xc2 = x0 + tL * dx
        yc2 = y0 + tL * dy

        print(f"Clipped at point ({xc1}, {yc1}), ({xc2}, {yc2})")

    elif tE == tL:
        x = x0 + tE * dx
        y = y0 + tE * dy

        print(f"Clipped at point ({x}, {y})")

    else:
        print("Line Completely outside")


x_min, y_min = 4, 4
x_max, y_max = 10, 8

#CyrusClipping(3, 3, 3, 3)
CyrusClipping(7, 9, 11, 4)
#CyrusClipping(1, 5, 4, 1)