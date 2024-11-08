// Define the clipping window boundaries
const xmin = 10,
  ymin = 10,
  xmax = 30,
  ymax = 20;

// Define region codes
const INSIDE = 0; // 0000
const LEFT = 1; // 0001
const RIGHT = 2; // 0010
const BOTTOM = 4; // 0100
const TOP = 8; // 1000

// Function to compute the region code for a point (x, y)
function computeOutcode(x, y) {
  let code = INSIDE;
  if (x < xmin) code |= LEFT;
  else if (x > xmax) code |= RIGHT;
  if (y < ymin) code |= BOTTOM;
  else if (y > ymax) code |= TOP;
  return code;
}

// Function implementing the Cohen-Sutherland algorithm
function cohenSutherlandClip(x1, y1, x2, y2) {
  let outcode1 = computeOutcode(x1, y1);
  let outcode2 = computeOutcode(x2, y2);
  let accept = false;

  while (true) {
    if (!(outcode1 | outcode2)) {
      accept = true;
      break;
    } else if (outcode1 & outcode2) {
      break;
    } else {
      let x, y;
      const outcodeOut = outcode1 ? outcode1 : outcode2;

      if (outcodeOut & TOP) {
        x = x1 + ((x2 - x1) * (ymax - y1)) / (y2 - y1);
        y = ymax;
      } else if (outcodeOut & BOTTOM) {
        x = x1 + ((x2 - x1) * (ymin - y1)) / (y2 - y1);
        y = ymin;
      } else if (outcodeOut & RIGHT) {
        y = y1 + ((y2 - y1) * (xmax - x1)) / (x2 - x1);
        x = xmax;
      } else if (outcodeOut & LEFT) {
        y = y1 + ((y2 - y1) * (xmin - x1)) / (x2 - x1);
        x = xmin;
      }

      if (outcodeOut === outcode1) {
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

  if (accept) {
    console.log(`Line accepted from (${x1}, ${y1}) to (${x2}, ${y2})`);
  } else {
    console.log("Line rejected");
  }
}

// Test the function with an example line segment
cohenSutherlandClip(5, 5, 25, 25);
