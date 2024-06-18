#!/usr/bin/python
import math
import tkinter

from PIL import Image, ImageTk

from ray import Ray
from vec3 import Vec3

WIDTH = 800
HEIGHT = 400
# Maybe want to calculate an aspect ratio?


# Basic "hittable" sphere
def hit_sphere(center, radius, ray):
    oc = ray.origin - center
    a = ray.direction.dot(ray.direction)
    b = 2.0 * oc.dot(ray.direction)
    c = oc.dot(oc) - radius ** 2
    discriminant = b**2 - 4*a*c
    if (discriminant < 0):
        return -1.0
    return (-b - math.sqrt(discriminant)) / (2.0*a)

# Cast ray and return a color vector
def color(ray):
    t = hit_sphere(Vec3(z=-1.0), 0.5, ray)
    if (t > 0.0):
        normal = (ray.point_at_parameter(t) - Vec3(z=-1.0)).unit_vector()
        return (normal+1)*0.5
    unit_direction = ray.direction.unit_vector()
    t = (unit_direction.y + 1.0) * 0.5  # Really shouldn't reuse variables like this
    return  Vec3.from_scalar(1.0)*(1.0 - t) + Vec3(0.5, 0.7, 1.0)*t


### MAIN FUNCTION ###

# Camera stuff
# Define the virtual screen area and the camera origin
lower_left_corner = Vec3(-2.0, -1.0, -1.0)
horizontal = Vec3(x=4.0)
vertical = Vec3(y=2.0)
origin = Vec3()

# Set up GUI
top = tkinter.Tk()
canvas = tkinter.Canvas(top, bg="blue", height=HEIGHT, width=WIDTH)
canvas.pack()

# Build Image
pilImage = Image.new('RGB', (WIDTH, HEIGHT), "black")
pixels = pilImage.load()

for y in range(pilImage.size[1]):
    for x in range(pilImage.size[0]):
        u = float(x) / float(pilImage.size[0])
        v = float(y) / float(pilImage.size[1])

        ray = Ray(origin, lower_left_corner + horizontal*u + vertical*v)
        col = color(ray)

        col *= 255.99
        pixels[x,y] = (int(col.r), int(col.g), int(col.b))

# Set up image widget
image = ImageTk.PhotoImage(pilImage)
image_sprite = canvas.create_image((1, 1), image=image, anchor="nw")

top.mainloop()
