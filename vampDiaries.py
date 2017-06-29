from PIL import Image

##Functions



#def overExpose(pixel):
##    red = pixel[0]
##    green = pixel[1]
##    blue = pixel[2]
##
##
##    newRed = red*2
##    if newRed > 255:
##        newRed = 255
##
##    newGreen = green*2
##    if newGreen > 255:
##        newGreen = 255
##
##    newBlue = blue*2
##    if newBlue > 255:
##        newBlue = 255
##    p = (newRed,newGreen,newBlue)
##    newpixelList.append(p)
##


#import the image
myImage= Image.open("elenaGilbert.jpeg")
imageData = myImage.getdata ()
pixelList= list(imageData)

##Function
#def darkBlue:
    
    #new.append(p)

    
newpixelList=[]


    
##red=pixel[0]
##green=pixel[1]
##blue=pixel[2]
##intensity=red+green+blue
##darkBlue=(0,51,76)
##red=(217,26,33)
##lightBlue=(112,150,158)
##yellow=(252,227,166)

    #find pixel intensity
for pixel in pixelList:
    
    
    red=pixel[0]
    green=pixel[1]
    blue=pixel[2]
    intensity=red+green+blue
    darkBlue=(0,51,76)
    red=(217,26,33)
    lightBlue=(112,150,158)
    yellow=(252,227,166)


    
    #if statement based on pixel intensity
    if intensity<182:
        newpixelList.append(darkBlue)
    elif 182 < intensity and intensity < 364:
        newpixelList.append(red)
    elif 546 < intensity and intensity >364:
        newpixelList.append(lightBlue)
    else:
        newpixelList.append(yellow)
        
        #(inside if statement)make new pixel
    #add pixel to newpixelList

   
    



#create new pixel


    

   
    
    



#add pixel to new pixel list
    

#open the image
newImage=Image.new("RGB",myImage.size)
newImage.putdata(newpixelList)
newImage.show()
#newImage.save("newPhoto.jpeg","jpeg")
