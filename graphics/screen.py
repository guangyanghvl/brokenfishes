import tkinter
from tkinter import *
class Screen:
    def __init__(self, width, height, title, background):
        #calculate center of screen
        self.zeros = [int(width/2), int(height/2)]

        #initialize tkinter window for displaying graphics
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.wm_attributes('-alpha', 0.7)
        self.image = tkinter.Canvas(self.window, width=0.8*width, height=height, bg='blue')
        self.image.pack(side='right', anchor='ne', ipady=10)

        input_frame = tkinter.Frame(self.window, relief=RAISED, borderwidth=1)
        input_frame.pack(side='left', expand=True, anchor='nw')

        # canvas_frame = tkinter.Frame(self.window, relief=RAISED, borderwidth=1)
        # canvas_frame.pack(side='right', anchor='ne', ipady=10)

        Label(input_frame)
       # h_backgroundCanvas = Canvas(canvas_frame, width=230, height=245, bg='white')
       # h_backgroundCanvas.grid(row=2, column=1, padx=50, pady=5)
       # h_canvas = Canvas(canvas_frame, width=200, height=215, bg='white')
       # h_canvas.grid(row=2, column=1, padx=50, pady=5)

        # Vertical Canvas
        #v_backgroundCanvas = Canvas(canvas_frame, width=230, height=230, bg='white')
        #v_backgroundCanvas.grid(row=1, column=1, padx=50, pady=5)
        #v_canvas = Canvas(canvas_frame, width=200, height=200, bg='grey')
        #v_canvas.grid(row=1, column=1, padx=50, pady=5)

        #v_canvas = tkinter.Canvas(self.window, width=200, height=200, bg='yellow')
        #v_canvas.pack()
        # v_canvas = self.image
        # Labels input
        Label(input_frame, text="Legg inn Koordinater: ").grid(row=0, column=0, columnspan=2, padx=35)
        Label(input_frame, text="Live stats/info").grid(row=0, column=4)
        xLabel = Label(input_frame, text="x - ").grid(row=1, column=0, sticky='E')
        yLabel = Label(input_frame, text="y - ").grid(row=2, column=0, sticky='E')
        zLabel = Label(input_frame, text="z - ").grid(row=3, column=0, sticky='E')
        depthLabel = Label(input_frame, text="Dybde: ").grid(row=1, column=3)
        currentLabel = Label(input_frame, text="Strøm: ").grid(row=2, column=3)
        tempLabel = Label(input_frame, text="Temp: ").grid(row=3, column=3)
        liveLabel = Label(input_frame, text="Live: ").grid(row=4, column=3)

        # Labels fixed units
        mLabel = Label(input_frame, text="m")
        mLabel.grid(row=1, column=5)

        msLabel = Label(input_frame, text="m/s")
        msLabel.grid(row=2, column=5)

        cdegLabel = Label(input_frame, text='c' + u'\u00b0')
        cdegLabel.grid(row=3, column=5)

        # x-coord entry box
        xEntry = Entry(input_frame, width=10)
        xEntry.grid(row=1, column=1, padx=10, pady=5, sticky='W')

        # y-coord entry box
        yEntry = Entry(input_frame, width=10)
        yEntry.grid(row=2, column=1, padx=10, pady=5, sticky='W')

        # z-coord entry box
        zEntry = Entry(input_frame, width=10)
        zEntry.grid(row=3, column=1, padx=10, pady=5, sticky='W')

        # Depth output label
        dOutput = Entry(input_frame, width=10)
        dOutput.grid(row=1, column=4, padx=10, pady=5)
        dOutput.insert(0, '0')

        # Current output label
        sOutput = Entry(input_frame, width=10)
        sOutput.grid(row=2, column=4, padx=10, pady=5)
        sOutput.insert(0, '0')

        # Temp output label
        tOutput = Entry(input_frame, width=10)
        tOutput.grid(row=3, column=4, padx=10, pady=5)
        tOutput.insert(0, '0')

        # Create balls
      #  hBall = h_canvas.create_oval(95, 102.5, 105, 112.5, fill='red', tag='hBall')
      #  vBall = v_canvas.create_oval(95, 95, 105, 105, fill='red', tag='vBall')
        lLabel = Label(input_frame, text="(0" + " , " + "0" + " , " + "0)")

        # Create arrows
       # hArrowX = h_backgroundCanvas.create_line(8, 240, 230, 240, arrow=LAST, width=3)
       # hArrowY = h_backgroundCanvas.create_line(8, 240, 8, 5, arrow=LAST, width=3)

       # vArrowX = v_backgroundCanvas.create_line(8, 225, 230, 225, arrow=LAST, width=3)
       # vArrowZ = v_backgroundCanvas.create_line(8, 225, 8, 5, arrow=LAST, width=3)

        # Live label
        lLabel.grid(row=4, column=4, pady=5)
    
    def createTriangle(self, points, color):
        a, b, c = points[0], points[1], points[2]
        #create coordinates starting in center of screen
        coords = [a[0] + self.zeros[0], a[1] + self.zeros[1], b[0] + self.zeros[0], b[1] + self.zeros[1], c[0] + self.zeros[0], c[1] + self.zeros[1]]
        #draw triangle on screen
        self.image.create_polygon(coords, fill=color, outline="black")

    def createLine(self, points, color):
        a, b = points[0], points[1]
        return self.image.create_line(a[0], a[1], b[0], b[1], fill=color, arrow=tkinter.BOTH)

    def clear(self):
        #clear display
        self.image.delete('all')

    def delete(self, item):
        self.image.delete(item)
        return None

    def after(self, time, function):
        #call tk.Tk's after() method
        self.window.after(time, function)
