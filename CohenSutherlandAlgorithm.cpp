#include <iostream>
using namespace std;

// Define the clipping window boundaries
const int xmin = 10, ymin = 10, xmax = 30, ymax = 20;

// Define region codes using bitwise positions
const int INSIDE = 0;   // 0000
const int LEFT = 1;     // 0001
const int RIGHT = 2;    // 0010
const int BOTTOM = 4;   // 0100
const int TOP = 8;      // 1000

// Function to compute the region code for a point (x, y)
int computeOutcode(int x, int y) {
    int code = INSIDE;

    if (x < xmin) code |= LEFT;
    else if (x > xmax) code |= RIGHT;
    if (y < ymin) code |= BOTTOM;
    else if (y > ymax) code |= TOP;

    return code;
}

// Function implementing the Cohen-Sutherland algorithm
void cohenSutherlandClip(int x1, int y1, int x2, int y2) {
    // Compute the initial outcodes for the two endpoints
    int outcode1 = computeOutcode(x1, y1);
    int outcode2 = computeOutcode(x2, y2);

    bool accept = false;

    while (true) {
        if ((outcode1 | outcode2) == 0) { // Both points are inside
            accept = true;
            break;
        } else if (outcode1 & outcode2) { // Both points are outside (in the same region)
            break;
        } else {
            // The line needs clipping
            int x, y;

            // Select the endpoint outside the window
            int outcodeOut = outcode1 ? outcode1 : outcode2;

            // Find the intersection point
            if (outcodeOut & TOP) { // Point is above the clipping window
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1);
                y = ymax;
            } else if (outcodeOut & BOTTOM) { // Point is below the clipping window
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1);
                y = ymin;
            } else if (outcodeOut & RIGHT) { // Point is to the right of the clipping window
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1);
                x = xmax;
            } else if (outcodeOut & LEFT) { // Point is to the left of the clipping window
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1);
                x = xmin;
            }

            // Update the outside point
            if (outcodeOut == outcode1) {
                x1 = x;
                y1 = y;
                outcode1 = computeOutcode(x1, y1);
            } else {
                x2 = x;
                y2 = y;
                outcode2 = computeOutcode(x2, y2);
            }
        }
    }

    // Output the result
    if (accept) {
        cout << "Line accepted from (" << x1 << ", " << y1 << ") to (" << x2 << ", " << y2 << ")" << endl;
    } else {
        cout << "Line rejected" << endl;
    }
}

// Main function to test the clipping algorithm
int main() {
    int x1 = 5, y1 = 5, x2 = 25, y2 = 25;
    cohenSutherlandClip(x1, y1, x2, y2);

    return 0;
}
