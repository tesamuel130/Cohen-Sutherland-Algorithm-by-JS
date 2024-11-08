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
    # Compute the initial outCodes for the two endpoints
    outCode1 = compute_outCode(x1, y1)
    outCode2 = compute_outCode(x2, y2)

    accept = False

    while True:
        if not (outCode1 | outCode2):
            # Both points are inside the clipping window, trivially accept
            accept = True
            break
        elif outCode1 & outCode2:
            # Both points share an outside region, trivially reject
            break
        else:
            # The line needs clipping
            x, y = 0.0, 0.0

            # Choose an endpoint outside the clipping window
            outCode_out = outCode1 if outCode1 else outCode2

            # Find the intersection point using the outCode
            if outCode_out & TOP:  # Point is above the clipping window
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif outCode_out & BOTTOM:  # Point is below the clipping window
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif outCode_out & RIGHT:  # Point is to the right of the clipping window
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif outCode_out & LEFT:  # Point is to the left of the clipping window
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            # Update the endpoint outside the clipping window
            if outCode_out == outCode1:
                x1, y1 = x, y
                outCode1 = compute_outCode(x1, y1)
            else:
                x2, y2 = x, y
                outCode2 = compute_outCode(x2, y2)

    # Output the result
    if accept:
        print(f"Line accepted from ({x1:.2f}, {y1:.2f}) to ({x2:.2f}, {y2:.2f})")
    else:
        print("Line rejected")

# Test the function with an example line segment
cohen_sutherland_clip(5, 5, 25, 25)
