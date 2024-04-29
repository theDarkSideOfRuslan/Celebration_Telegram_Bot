from PIL import Image, ImageDraw, ImageFont

def new_year(by, to):
    image1 = Image.open("data/NewYear/NewYear1.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 15)
    drawer = ImageDraw.Draw(image1)
    drawer.text((10, 560), f"от: {by}\nкому: {to}", font=font, fill=(128, 0, 0))
    image1.save('data/NewYear/NewYear11.jpg')
    image1.close()

    image2 = Image.open("data/NewYear/NewYear3.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 30)
    drawer = ImageDraw.Draw(image2)
    drawer.text((10, 950), f"от: {by}\nкому: {to}", font=font, fill=(250, 0, 0))
    image2.save('data/NewYear/NewYear33.jpg')
    image2.close()

    image3 = Image.open("data/NewYear/NewYear4.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 30)
    drawer = ImageDraw.Draw(image3)
    drawer.text((10, 10), f"от: {by}\nкому: {to}", font=font, fill=(250, 0, 0))
    image3.save('data/NewYear/NewYear44.jpg')
    image3.close()

    image4 = Image.open("data/NewYear/NewYear5.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 45)
    drawer = ImageDraw.Draw(image4)
    drawer.text((30, 1490), f"от: {by}\nкому: {to}", font=font, fill=(250, 0, 0))
    image4.save('data/NewYear/NewYear55.jpg')
    image4.close()


def birthday(by, to):
    image1 = Image.open("data/Birthday/Birthday1.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 15)
    drawer = ImageDraw.Draw(image1)
    drawer.rectangle((0, 360, max(len(f"от: {by}"), len(f"кому: {to}"))*10.5, 400), 'white')
    drawer.text((5, 360), f"от: {by}\nкому: {to}", font=font, fill=(128, 0, 0))
    image1.save('data/Birthday/Birthday11.jpg')
    image1.close()


    image2 = Image.open("data/Birthday/Birthday2.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 15)
    drawer = ImageDraw.Draw(image2)
    drawer.rectangle((0, 360, max(len(f"от: {by}"), len(f"кому: {to}"))*10.5, 400), 'white')
    drawer.text((5, 360), f"от: {by}\nкому: {to}", font=font, fill=(128, 0, 0))
    image2.save('data/Birthday/Birthday22.jpg')
    image2.close()


def march8th(by, to):
    image1 = Image.open("data/March8th/March8th1.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 50)
    drawer = ImageDraw.Draw(image1)
    drawer.text((5, 1080), f"от: {by}\nкому: {to}", font=font, fill=(120,81,169))
    image1.save('data/March8th/March8th11.jpg')
    image1.close()

    image2 = Image.open("data/March8th/March8th2.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 30)
    drawer = ImageDraw.Draw(image2)
    drawer.rectangle((900 - max(len(f"от: {by}"), len(f"кому: {to}"))*20, 830, 900, 900), 'white')
    drawer.text((905 - max(len(f"от: {by}"), len(f"кому: {to}"))*20, 830), f"от: {by}\nкому: {to}", font=font, fill='#fc0fc0')
    image2.save('data/March8th/March8th22.jpg')
    image2.close()