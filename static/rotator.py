from PIL import Image
import imageio

img = Image.open('logo.png')
angle = 1
image = []
for i in range(1, 361):
    rotated_img = img.rotate(angle)
    rotated_img.save(f'Image of Angle {angle}.png')
    angle += 1






