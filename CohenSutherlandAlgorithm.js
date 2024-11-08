// Define the clipping window boundaries
const xMin = 10,
  yMin = 10,
  xMax = 30,
  yMax = 20;

// Define region codes
const INSIDE = 0; // 0000
const LEFT = 1; // 0001
const RIGHT = 2; // 0010
const BOTTOM = 4; // 0100
const TOP = 8; // 1000

// Function to compute the region code for a point (x, y)
function computeOutCode(x, y) {
  let code = INSIDE;
  if (x < xMin) code |= LEFT;
  else if (x > xMax) code |= RIGHT;
  if (y < yMin) code |= BOTTOM;
  else if (y > yMax) code |= TOP;
  return code;
}

// Function implementing the Cohen-Sutherland algorithm
function cohenSutherlandClip(x1, y1, x2, y2) {
  let outCode1 = computeOutCode(x1, y1);
  let outCode2 = computeOutCode(x2, y2);
  let accept = false;

  while (true) {
    if (!(outCode1 | outCode2)) {
      accept = true;
      break;
    } else if (outCode1 & outCode2) {
      break;
    } else {
      let x, y;
      const outCodeOut = outCode1 ? outCode1 : outCode2;

      if (outCodeOut & TOP) {
        x = x1 + ((x2 - x1) * (yMax - y1)) / (y2 - y1);
        y = yMax;
      } else if (outCodeOut & BOTTOM) {
        x = x1 + ((x2 - x1) * (yMin - y1)) / (y2 - y1);
        y = yMin;
      } else if (outCodeOut & RIGHT) {
        y = y1 + ((y2 - y1) * (xMax - x1)) / (x2 - x1);
        x = xMax;
      } else if (outCodeOut & LEFT) {
        y = y1 + ((y2 - y1) * (xMin - x1)) / (x2 - x1);
        x = xMin;
      }

      if (outCodeOut === outCode1) {
        x1 = x;
        y1 = y;
        outCode1 = computeOutCode(x1, y1);
      } else {
        x2 = x;
        y2 = y;
        outCode2 = computeOutCode(x2, y2);
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
