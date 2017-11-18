import os.path
import pygame
from tkinter import Tk, filedialog
from PLogic import LogicSim, Grid, Label, Color


def save(simulator):
    filename = filedialog.asksaveasfilename(filetypes=(("P-Logic scene", "*.pls"),))
    if len(filename) > 0:
        if not filename.endswith(".pls"):
            filename += ".pls"
        with open(filename, 'w') as file:
            file.write(simulator.save_scene())


def load(simulator):
    filename = filedialog.askopenfilename(filetypes=(("P-Logic scene", "*.pls"),))

    if not os.path.isfile(filename):
        return

    data = None
    with open(filename) as file:
        data = file.read()
    simulator.load_scene(data)


# Init simulator

simulator = LogicSim()
simulator.init("assets/", save, load)

# Init gui

root = Tk()
root.withdraw()

grid = Grid()
simulator.scene.register_object(grid)

pygame.font.init()
font = pygame.font.SysFont('Arial', 18)
label = Label("[1]AND [2]OR [3]XOR, [4]NOR [5]XNOR [6]NAND [7]NOT [8]SWITCH [9]LIGHT [0]LOGIC 1 [Q]Clock [W]PIN", font,
              30, (0, 0), Color.Orange)

simulator.scene.register_object(label)

# Run simulator

simulator.run()
