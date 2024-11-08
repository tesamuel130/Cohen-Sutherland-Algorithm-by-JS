# Cohen-Sutherland-Algorithm-by-JS
This repository contains a JavaScript implementation of the Cohen-Sutherland Line Clipping Algorithm, a fundamental computer graphics algorithm used for line clipping in 2D graphics. This algorithm is particularly useful for rendering scenes efficiently by determining if a line segment lies inside, outside, or partially within a specified rectangular clipping window.

# Overview
The Cohen-Sutherland algorithm is used to efficiently determine whether a line segment should be drawn within a specific region of the screen (the clipping window). If a line segment lies outside of this window, it can be ignored, saving computational resources. If it lies partially inside, the algorithm calculates where it intersects the clipping window and only displays the visible portion.

# Algorithm Explanation
The algorithm works as follows:

1. Each endpoint of the line segment is assigned a 4-bit region code. Each bit represents a direction (LEFT, RIGHT, TOP, BOTTOM) in relation to the clipping window.
2. The algorithm then uses these codes to:
    * Trivially accept the line if both endpoints are inside the window.
    * Trivially reject the line if both endpoints lie outside the window in the same region.
    * Calculate intersections with the clipping window if the line partially intersects it.

# Region Code Bitmask
Each region around the window is represented by a bit:

* 0001: Left of the window
* 0010: Right of the window
* 0100: Below the window
* 1000: Above the window