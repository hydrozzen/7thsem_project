from PIL import Image,ImageDraw,ImageFont

image = Image.open("medical.png")

d= ImageDraw.Draw(image)

font = ImageFont.truetype("BRADHITC.TTF",380)

#patient_name="Patient name"
patient_name=input("Enter the name jiska fake cerificate chiyae")

patient_name_pos=(1920,2820)
patient_name_color = (0,0,0)

d.text(patient_name_pos,text=patient_name,fill=patient_name_color,font=font)



#disease_name="disease name"
disease_name=input("Enter the disease name jiska fake cerificate chiyae")
font1 = ImageFont.truetype("BRADHITC.TTF",280)

disease_name_pos=(3720,3520)
disease_name_color = (0,0,0)

d.text(disease_name_pos,text=disease_name,fill=disease_name_color,font=font1)


#Startdate_name="11/11/2011"
Startdate_name=input("Enter the starting date fake cerificate kae liye")
font2 = ImageFont.truetype("BRADHITC.TTF",190)

Startdate_name_pos=(870,4690)
Startdate_name_color = (0,0,0)

d.text(Startdate_name_pos,text=Startdate_name,fill=Startdate_name_color,font=font2)


#Enddate_name="11/11/3011"
Enddate_name=input("Enter the ending date fake cerificate kae liye")
font3 = ImageFont.truetype("BRADHITC.TTF",190)

Enddate_name_pos=(2090,4690)
Enddate_name_color = (0,0,0)

d.text(Enddate_name_pos,text=Enddate_name,fill=Enddate_name_color,font=font3)

#Date_name="11/11/2011"
Date_name=input("Enter the date jab ka fake cerificate chiyae")
font2 = ImageFont.truetype("BRADHITC.TTF",190)

Date_name_pos=(870,5790)
Date_name_color = (0,0,0)

d.text(Date_name_pos,text=Date_name,fill=Date_name_color,font=font)



image.save(f"{patient_name}_certified.png")
print("done,aapka fake medical certificate bn gya!!!!!!")