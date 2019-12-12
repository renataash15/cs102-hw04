import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

# Create a new, all-white image that's the same size as the original
new_img = Image.new("RGB", (width, height), "white")
 
for i in range(1, width-1):
    if not i % 10:
        print(f"processing col {i}")
    for j in range(1, height-1):
        r, g, b = img.getpixel((i, j))
        if r < 205:
            r = r + 50
        else:
            r = 255
        if b < 205:
            b = b + 50
        else:
            b = 255
        new_img.putpixel((i, j), (r, g, b))

new_img.save(output_path)
