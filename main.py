from PIL import Image, ImageDraw, ImageFont
import textwrap
from slugify import slugify

# img = Image.new('RGB', (400, 277), color='black')
# d = ImageDraw.Draw(img)
# font = ImageFont.truetype('./assets/Helvetica-Font/Helvetica.ttf', 40)
# d.text((30, 30), "Basic programs to install on raspberry by terminal", fill=(255, 255, 255), font=font)
#
astr = ''' Contamos con tus 5 sol-sasoss o no xD... '''
para = textwrap.wrap(astr, width=25)

MAX_W, MAX_H = 400, 277
im = Image.new('RGB', (MAX_W, MAX_H), (0, 0, 0, 0))
draw = ImageDraw.Draw(im)
font = ImageFont.truetype(
    './assets/font/Helvetica.ttf', 30)

current_h, pad = 70, 10
for line in para:
    w, h = draw.textsize(line, font=font)
    # w, h = draw.textlength(line, font=font)
    draw.text(((MAX_W - w) / 2, current_h), line, font=font)
    current_h += h + pad
#
file_name = slugify(astr)
im.save(file_name + '-400x277.png')