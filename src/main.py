"""
Adam Klekowski (AGH UST)

Project developed for Scripting Languages class.

A task of application is to draw a film from Filmweb website.
A user can specify details, such as category and minimal rate.
Films marked as viewed by user are skipped during the drawing.
"""

from File import *
from GUI import GUI

if __name__ == "__main__":
    f = File()
    g = GUI(f)
    g.run()
    f.save()
