### Cube ###
from tkinter import *
import graphics.engine

points = [[-1,-1,-1],[-1,-1,1],[-1,1,1],[-1,1,-1],[1,-1,-1],[1,-1,1],[1,1,1],[1,1,-1]]
triangles = [[0,1,2],[0,2,3],[2,3,7],[2,7,6],[1,2,5],[2,5,6],[0,1,4],[1,4,5],[4,5,6],[4,6,7],[3,7,4],[4,3,0]]


pointRed = [20,15,15]
test = graphics.engine.Engine3D(points, pointRed, triangles, title='TestGUI')

def animation():
    test.clear()
    test.rotate('y', 0.1)
    test.rotate('x', 0.1)
    test.render()
    test.screen.after(1, animation)


test.screen.window.mainloop()
############
