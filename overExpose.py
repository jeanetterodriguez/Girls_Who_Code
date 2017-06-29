from PIL import Image


#Import the image and make pixel list
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)



newPixelList = []

#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]


    newRed = red*2
    if newRed > 255:
        newRed = 255

    newGreen = green*2
    if newGreen > 255:
        newGreen = 255

    newBlue = blue*2
    if newBlue > 255:
        newBlue = 255


    p = (newRed,newGreen,newBlue)
    
    #add pixel to new pixel list
    newPixelList.append(p)




#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
#newImage.save("newPhoto.jpeg","jpeg")
