# Import the required libraries
import tkinter
import json

# Opening JSON file
vertexFile = open('Vertices.json')

# returns JSON object as
# a dictionary
vertices = json.load(vertexFile)

# Iterating through the json
# list
for i in vertices['Vertices']:
	print(i)

# Closing file
vertexFile.close()

print

pathFile = open('Paths.json')

# returns JSON object as
# a dictionary
paths = json.load(pathFile)

# Iterating through the json
# list
for i in paths['Paths']:
	print(i)

# Closing file
pathFile.close()


# Create an instance of tkinter frame or window
win = tkinter.Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create a canvas widget
canvas= tkinter.Canvas(win, width=500, height=300)
canvas.pack()

# Add a line in canvas widget
for i in paths['Paths']:
    V = vertices['Vertices']
    canvas.create_line( V[i[0]][0], V[i[0]][1], V[i[1]][0] , V[i[1]][1], fill="green", width=5)

win.mainloop()