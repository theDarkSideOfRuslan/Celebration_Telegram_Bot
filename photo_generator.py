from PIL import Image, ImageDraw, ImageFont

def new_year(by, to, id):
    image1 = Image.open("data/NewYear/NewYear1.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 15)
    drawer = ImageDraw.Draw(image1)
    drawer.text((10, 560), f"от: {by}\nкому: {to}", font=font, fill=(128, 0, 0))
    image1.save(f'data/NewYear/NewYear1_{id}.jpg')
    image1.close()

    image2 = Image.open("data/NewYear/NewYear3.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 30)
    drawer = ImageDraw.Draw(image2)
    drawer.text((10, 950), f"от: {by}\nкому: {to}", font=font, fill=(250, 0, 0))
    image2.save(f'data/NewYear/NewYear2_{id}.jpg')
    image2.close()

    image3 = Image.open("data/NewYear/NewYear4.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 30)
    drawer = ImageDraw.Draw(image3)
    drawer.text((10, 10), f"от: {by}\nкому: {to}", font=font, fill=(250, 0, 0))
    image3.save(f'data/NewYear/NewYear3_{id}.jpg')
    image3.close()

    image4 = Image.open("data/NewYear/NewYear5.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 45)
    drawer = ImageDraw.Draw(image4)
    drawer.text((30, 1490), f"от: {by}\nкому: {to}", font=font, fill=(250, 0, 0))
    image4.save(f'data/NewYear/NewYear4_{id}.jpg')
    image4.close()


def birthday(by, to, id):
    image1 = Image.open("data/Birthday/Birthday1.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 15)
    drawer = ImageDraw.Draw(image1)
    drawer.rectangle((0, 360, max(len(f"от: {by}"), len(f"кому: {to}"))*10.5, 400), 'white')
    drawer.text((5, 360), f"от: {by}\nкому: {to}", font=font, fill=(128, 0, 0))
    image1.save(f'data/Birthday/Birthday1_{id}.jpg')
    image1.close()


    image2 = Image.open("data/Birthday/Birthday2.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 15)
    drawer = ImageDraw.Draw(image2)
    drawer.rectangle((0, 360, max(len(f"от: {by}"), len(f"кому: {to}"))*10.5, 400), 'white')
    drawer.text((5, 360), f"от: {by}\nкому: {to}", font=font, fill=(128, 0, 0))
    image2.save(f'data/Birthday/Birthday2_{id}.jpg')
    image2.close()


def march8th(by, to, id):
    image1 = Image.open("data/March8th/March8th1.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 50)
    drawer = ImageDraw.Draw(image1)
    drawer.text((5, 1080), f"от: {by}\nкому: {to}", font=font, fill=(120,81,169))
    image1.save(f'data/March8th/March8th1_{id}.jpg')
    image1.close()

    image2 = Image.open("data/March8th/March8th2.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 30)
    drawer = ImageDraw.Draw(image2)
    drawer.rectangle((900 - max(len(f"от: {by}"), len(f"кому: {to}"))*20, 830, 900, 900), 'white')
    drawer.text((905 - max(len(f"от: {by}"), len(f"кому: {to}"))*20, 830), f"от: {by}\nкому: {to}", font=font, fill='#fc0fc0')
    image2.save(f'data/March8th/March8th2_{id}.jpg')
    image2.close()

def February23rd(by, to, id):
    image1 = Image.open("data/February23rd/February23rd1.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 20)
    drawer = ImageDraw.Draw(image1)
    drawer.text((5, 560), f"от: {by}\nкому: {to}", font=font, fill='white')
    image1.save(f'data/February23rd/February23rd1_{id}.jpg')
    image1.close()


    image2 = Image.open("data/February23rd/February23rd2.jpg")
    font = ImageFont.truetype("data/fonts/TransformaScript_Trial-Regular.ttf", 20)
    drawer = ImageDraw.Draw(image2)
    drawer.rectangle((604 - max(len(f"от: {by}"), len(f"кому: {to}"))*15, 545, 604, 604), 'white')
    drawer.text((609 - max(len(f"от: {by}"), len(f"кому: {to}"))*14.5, 550), f"от: {by}\nкому: {to}", font=font, fill='red')
    image2.save(f'data/February23rd/February23rd2_{id}.jpg')
    image2.close()


def May1st(by, to, id):
    image1 = Image.open("data/May1st/May1st1.jpg")
    font = ImageFont.truetype("data/fonts/Stengazeta-Regular_5.ttf", 50)
    drawer = ImageDraw.Draw(image1)
    drawer.text((5, 850), f"от: {by}\nкому: {to}", font=font, fill='black')
    image1.save(f'data/May1st/May1st1_{id}.jpg')
    image1.close()

    image2 = Image.open("data/May1st/May1st2.jpg")
    font = ImageFont.truetype("data/fonts/Stengazeta-Regular_5.ttf", 60)
    drawer = ImageDraw.Draw(image2)
    drawer.text((5, 845), f"от: {by}   кому: {to}", font=font, fill='white')
    image2.save(f'data/May1st/May1st2_{id}.jpg')
    image2.close()