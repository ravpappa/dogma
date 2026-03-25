#!/usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt

from tkinter import *
from tkhtmlview import HTMLLabel

root = Tk()
root.geometry("1100x900")

#print("Hello world!") 
titre = HTMLLabel(root,html="<h1>Hello world</h1>")
titre.place(x=10,y=20)

root.mainloop()


#fig,ax=plt.subplots(subplot_kw={"projection":"3d"})
#X=np.arange(-5,5,.25)
#Y=np.arange(-5,5,.25)
#X,Y=np.meshgrid(X,Y)
#Z=np.sin(np.sqrt(X**2+Y**2))
#surf=ax.plot_surface(X,Y,Z)
#plt.show()

