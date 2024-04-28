from PIL import Image, ImageDraw, ImageFont

def new_year(by, to):
    image = Image.open("data/NewYear/NewYear1.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 15)
    drawer = ImageDraw.Draw(image)
    drawer.text((10, 560), f"от: {by}\nкому: {to}", font=font, fill=(128, 0, 0))
    image.save('data/NewYear/NewYear11.jpg')
    image.show()
    image.close()

    image = Image.open("data/NewYear/NewYear3.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 30)
    drawer = ImageDraw.Draw(image)
    drawer.text((10, 950), f"от: {by}\nкому: {to}", font=font, fill=(250, 0, 0))
    image.save('data/NewYear/NewYear33.jpg')
    image.show()

    image = Image.open("data/NewYear/NewYear4.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 30)
    drawer = ImageDraw.Draw(image)
    drawer.text((10, 10), f"от: {by}\nкому: {to}", font=font, fill=(250, 0, 0))
    image.save('data/NewYear/NewYear44.jpg')
    image.show()

    image = Image.open("data/NewYear/NewYear5.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 45)
    drawer = ImageDraw.Draw(image)
    drawer.text((30, 1490), f"от: {by}\nкому: {to}", font=font, fill=(250, 0, 0))
    image.save('data/NewYear/NewYear55.jpg')
    image.show()
