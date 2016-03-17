from display import *
from matrix import *
import math

def add_circle(points, cx, cy, cz, r, step):
    x = cx + r
    y = cy + r
    t = 0
    while t < 1:
        points.add_point(points, x, y)
        x = cx + r * math.cos(2 * math.pi * t)
        y = cy + r * math.sin(2 * math.pi * t)
        points.add_point(points, x, y)
        t += step
    points.add_point(points, x, y)
    points.add_point(points, cx + r, cy + r)

def add_curve(points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type):
    name = curve_type.upper().lower()
    if name == "bezier":
        print "bezier detected"
    elif name == "hermite":
        print "hermite detected"
    else:
        print "Error: curve type unknown: " + curve_type

def draw_lines(matrix, screen, color):
    if len(matrix) < 2:
        print "Need at least 2 points to draw a line"
    
    for i in range(0, len(matrix), 2):
        draw_line(screen, matrix[i][0], matrix[i][1],
                  matrix[p+1][0], matrix[p+1][1], color)

def add_edge(matrix, x0, y0, z0, x1, y1, z1):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point(matrix, x, y, z=0):
    matrix.append([x, y, z, 1])

def draw_line(screen, x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0
    
    if dx + dy < 0:
        dx = -dx
        dy = -dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y += 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x += 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y -= 1
                d -= dx
            x += 1
            d -= dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x -= 1
                d -= dy
            y += 1
            d -= dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d -= dx
            x += 1
            d += dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x += 1
                d -= dy
            y += 1
            d += dx
