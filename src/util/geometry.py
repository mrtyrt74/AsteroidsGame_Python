from pygame import Rect


def calculateGradient(s1, s2):
    if s1[0] != s2[0]:
        m = (s1[1] - s2[1]) / (s1[0] - s2[0])
        return m
    else:
        return None

def calculateYAxisIntersect(p, m):
    return p[1] - (m * p[0])


def getIntersectPoint(s1, s2, s3, s4, false=None):
    global y, x
    m1 = calculateGradient(s2)
    m2 = calculateGradient(s4)

    if m1 != m2:

        # See if either line is vertical
        if m1 is not None and m2 is not None:
            # Neither line vertical
            b1 = calculateYAxisIntersect(s1, m1)
            b2 = calculateYAxisIntersect(s3, m2)
            x = (b2 - b1) / (m1 - m2)
            y = (m1 * x) + b1
        else:
            # Line 1 is vertical so use line 2's values
            if m1 is None:
                b2 = calculateYAxisIntersect(s3, m2)
                x = s1[0]
                y = (m2 * x) + b2
            # Line 2 is vertical so use line 1's values
            elif m2 is None:
                b1 = calculateYAxisIntersect(s1, m1)
                x = s3[0]
                y = (m1 * x) + b1
            else:
                assert false
        return (x, y),
    else:
        b1, b2 = None, None  # vertical lines have no b value
        if m1 is not None:
            b1 = calculateYAxisIntersect(s1, m1)

        if m2 is not None:
            b2 = calculateYAxisIntersect(s3, m2)

        # If these parallel lines lay on one another
        if b1 == b2:
            return s1, s2, s3, s4
        else:
            return None


def calculateIntersectPoint(s1, s2, s3, s4):
    p = getIntersectPoint(s1, s2, s3, s4)

    if p is not None:
        width = s2[0] - s1[0]
        height = s2[1] - s1[1]
        r1 = Rect(s1, (width, height))
        r1.normalize()

        width = s4[0] - s3[0]
        height = s4[1] - s3[1]
        r2 = Rect(s3, (width, height))
        r2.normalize()
        tolerance = 1
        if r1.width < tolerance:
            r1.width = tolerance

        if r1.height < tolerance:
            r1.height = tolerance

        if r2.width < tolerance:
            r2.width = tolerance

        if r2.height < tolerance:
            r2.height = tolerance

        for point in p:
            try:
                res1 = r1.collidepoint(point)
                res2 = r2.collidepoint(point)
                if res1 and res2:
                    point = [int(pp) for pp in point]
                    return point
            except:
                # sometimes the value in a point are too large for PyGame's Rect class
                str = "point was invalid  ", point
                print(str)

        return None

    else:
        return None


# Test script below...
if __name__ == "__main__":
    # line 1 and 2 cross, 1 and 3 don't but would if extended, 2 and 3 are parallel
    # line 5 is horizontal, line 4 is vertical
    p1 = (1, 5)
    p2 = (4, 7)

    p3 = (4, 5)
    p4 = (3, 7)

    p5 = (4, 1)
    p6 = (3, 3)

    p7 = (3, 1)
    p8 = (3, 10)

    p9 = (0, 6)
    p10 = (5, 6)

    p11 = (472.0, 116.0)
    p12 = (542.0, 116.0)

    assert None != calculateIntersectPoint(
        p1, p2, p3, p4), "line 1 line 2 should intersect"
    assert None != calculateIntersectPoint(
        p3, p4, p1, p2), "line 2 line 1 should intersect"
    assert None == calculateIntersectPoint(
        p1, p2, p5, p6), "line 1 line 3 shouldn't intersect"
    assert None == calculateIntersectPoint(
        p3, p4, p5, p6), "line 2 line 3 shouldn't intersect"
    assert None != calculateIntersectPoint(
        p1, p2, p7, p8), "line 1 line 4 should intersect"
    assert None != calculateIntersectPoint(
        p7, p8, p1, p2), "line 4 line 1 should intersect"
    assert None != calculateIntersectPoint(
        p1, p2, p9, p10), "line 1 line 5 should intersect"
    assert None != calculateIntersectPoint(
        p9, p10, p1, p2), "line 5 line 1 should intersect"
    assert None != calculateIntersectPoint(
        p7, p8, p9, p10), "line 4 line 5 should intersect"
    assert None != calculateIntersectPoint(
        p9, p10, p7, p8), "line 5 line 4 should intersect"

    print("\nSUCCESS! All asserts passed for doLinesIntersect")
