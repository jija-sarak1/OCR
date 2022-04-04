from PIL import Image
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
tool = tools[0]
langs = tool.get_available_languages()
lang = langs[0]
tool = pyocr.get_available_tools()[0]
builder = pyocr.builders.TextBuilder()
font = ['Ani','AnjaliOldLipi','caveat','Chilanka','KacstLetter','TlwgTypewriter','handwritten','handwritten1']
images = ['/home/jija/Desktop/files/newfile/images/Ani.png',
'/home/jija/Desktop/files/newfile/images/AnjaliOldLipi.png',
'/home/jija/Desktop/files/newfile/images/caveat.png',
'/home/jija/Desktop/files/newfile/images/Chilanka.png',
'/home/jija/Desktop/files/newfile/images/KacstLetter.png',
'/home/jija/Desktop/files/newfile/images/TlwgTypewriter.png',
'/home/jija/Desktop/files/newfile/images/handwritten.jpeg',
'/home/jija/Desktop/files/newfile/images/handwritten1.jpeg']
i = 0
while i < len(images):
    txt = tool.image_to_string(
        Image.open(images[i]),
        lang=lang,
        builder=builder
    )
    print(str(i+1) +".","Font" ,font[i],'\n','\n')
    print(txt)

    f = open(r"/home/jija/Desktop/files/newfile/output_folder/"+str(font[i]+"_img")+".txt", "w")
    f.write(txt)
    f.close()
    i+=1
