from PIL import Image
import PIL
import os

image = Image.open("image copy 2.png")
image.thumbnail((30, 30))
image.save("bullet.png")