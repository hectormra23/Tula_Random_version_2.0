#this code was created just for fun and no offense intended, it's a project/joke between me and my friends

#import libraries
from playsound import playsound 
from PIL import Image


#img varibales 
im1 = Image.open('img\wuaifu1.jfif')
im2 = Image.open('img\wuaifu2.jfif')
 
#variables
nombre=input("ingresa tu nombre")
medida=float(input("ingresa tu medida"))

#pinga bucle(loop)
if medida >= 10:
    print("tu pinga es grande mi pana")
    playsound("D:/tula/sound/yamete-kudasai.mp3")#poner la ruta desde donde se descargo al carpeta (solo cambia D:)
    im1.show()
else:
    print("tu pinga es chica :(")
    playsound("D:/tula/sound/sad.mp3")#poner la ruta desde donde se descargo al carpeta (solo cambia D:)
    im2.show()


#nota :

#abrir terminal en visual estudio e intalar las librerias:
#pip install --upgrade Pillow
#pip install playsound






