# Define the clipping window boundaries
xmin, ymin, xmax, ymax = 10, 10, 30, 20

# Define region codes using bitwise flags
INSIDE = 0    # 0000
LEFT = 1      # 0001
RIGHT = 2     # 0010
BOTTOM = 4    # 0100
TOP = 8       # 1000

# Function to compute the region code for a point (x, y)
def compute_outCode(x, y):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code

# Function implementing the Cohen-Sutherland algorithm
def cohen_sutherland_clip(x1, y1, x2, y2):
    outCode1 = compute_outCode(x1, y1)
    outCode2 = compute_outCode(x2, y2)

    accept = False

    while True:
        if not (outCode1 | outCode2):
            accept = True
            break
        elif outCode1 & outCode2:
            break
        else:
            x, y = 0.0, 0.0

            outCode_out = outCode1 if outCode1 else outCode2

            if outCode_out & TOP: 
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif outCode_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif outCode_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif outCode_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if outCode_out == outCode1:
                x1, y1 = x, y
                outCode1 = compute_outCode(x1, y1)
            else:
                x2, y2 = x, y
                outCode2 = compute_outCode(x2, y2)

    if accept:
        print(f"Line accepted from ({x1:.2f}, {y1:.2f}) to ({x2:.2f}, {y2:.2f})")
    else:
        print("Line rejected")

# Test the function with an example line segment
cohen_sutherland_clip(5, 5, 25, 25)
