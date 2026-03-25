from pyscript import web, when, display, HTML
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import re
import cmath as cm

def set_axes(ax):
    
    # Set axes limits
    x_lim = [-10,10]
    y_lim = [-10,10]
    ax.set_xlim(x_lim[0],x_lim[1])
    ax.set_ylim(y_lim[0],y_lim[1])

    # Set the axis ticks
    ax.set(xticks=[0],
        yticks=[0],
        zticks=[0])

    # Set the axis ticks labels
    ax.set(xticklabels=["0"],
        yticklabels=["0"],
        zticklabels=["0"])

    # Set the axis labels
    ax.set_xlabel('Re(z)')
    ax.set_ylabel('Im(z)')
    ax.set_zlabel('|f(z)|')

    ax.view_init(45,-90,0)

# Initialize the complex plane
if 'fig' not in globals():
    mouseDown = True
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    set_axes(ax) 
    display(fig, target="plot-output", append=False)

# Set the axis view
@when("mousemove", ".slider")
def angle_of_view(event):
    if mouseDown:
        global fig, ax
        sliders = web.page.find(".slider")
        for slider in sliders:
            match slider.id:
                case "sliderElev":
                    ax.elev = float(web.page["#sliderElevValue"].innerText) # Elevation
                case "sliderAzim":
                    ax.azim = float(web.page["#sliderAzimValue"].innerText) # Azimuth
                case "sliderRoll":
                    ax.roll = float(web.page["#sliderRollValue"].innerText) # Roll
        display(fig, target="plot-output", append=False)

@when("click", "#btn-plot")
def plot_function(event):

    global fig, ax
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    nb = 1000 # Number of bins along Re and Im axes
    X = np.linspace(-10, 10, nb) 
    Y = np.linspace(-10, 10, nb)
    X, Y = meshgrid(X,Y)

    function = web.page["function"]
    sub2do = {'i':'1j','\\^':'**'}
    myfunc = function.value
    for key, value in sub2do.items():
        myfunc = re.sub(key,value,myfunc)
    f = eval("lambda z:"+myfunc)
   
    vec_f = np.vectorize(f)
    Z = vec_f(X+np.multiply(Y,1j))
    vec_polar = np.vectorize(cm.polar)
    R, phi = vec_polar(Z)

    ax.plot_surface(X, Y, R, facecolors=plt.cm.jet((phi+pi)/2/pi))
    set_axes(ax)

    display(HTML("<h3>f(z)=</h3>"), target="plot-output", append=False)
    display(fig, target="plot-output", append=False)

