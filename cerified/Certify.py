from PIL import Image,ImageDraw,ImageFont

image = Image.open("certicate.png")

d= ImageDraw.Draw(image)

font = ImageFont.truetype("ITCEDSCR.TTF",650)

text="Sample Text"
#text=input("Enter the name jiska fake cerificate chiyae")

text_pos=(1620,1480)
text_color = (0,0,0)

d.text(text_pos,text=text,fill=text_color,font=font)

image.save(f"{text}_certified.png")