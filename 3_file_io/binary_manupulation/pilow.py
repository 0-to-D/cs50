import sys
from PIL import image

image_list = []

for arg in sys.argv[1:]:
    image = image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
