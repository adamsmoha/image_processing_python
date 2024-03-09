from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

print("Image: ", img)
print("Image format: ", img.format)
print("Image Size: ", img.size)
print("Image mode", img.mode)

# Blurring an image
blurred_image = img.filter(ImageFilter.BLUR)
blurred_image.save("./Pokedex/pikachu_Blurry.png", "png")

# converting an image
grayscaled_image = img.convert('L')  # convert to grayscale
grayscaled_image.save("./Pokedex/pikachu_GrayScale.png", "png")

# rotating image
rotated_image = img.rotate(-45)
rotated_image.save("./Pokedex/pikachu_Rotate.png", "png")

# display image in photo app
rotated_image.show()

# Resizing the image
thumbnail = img.resize((100, 100))
thumbnail.save("./Pokedex/pikachu_ThumbNail.png", "png")

# thumbnail method
img.thumbnail((32, 32))
img.save("./Pokedex/pikachu_Smaller.png", "png")


# crop image
region = (50, 20, 100, 80)   # left, upper, right and lower pixel index
croped_image = img.crop(region)
croped_image.save("./Pokedex/pikachu_Cropped.png", "png")
