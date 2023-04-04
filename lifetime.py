# -*- coding: utf-8 -*-
"""
@author: Björn Luig

A short script that generates a visualisation of all the weeks in life which you have lived and which you have left.
"""

from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont

# user imput
birthday = input("birthday (dd.mm.yyyy)? ").split(".")
lifetime = int(
    input(
        "life expectency in years (probably ~90 or for example look at https://www.livingto100.com/calculator)? "
    )
)

# get dates
today = datetime.now()
birthday = datetime(int(birthday[2]), int(birthday[1]), int(birthday[0]))
deathday = datetime(birthday.year + lifetime, birthday.month, birthday.day)

# make image
img = Image.new("RGB", (1000, 200 + 16 * (lifetime + 1) + 100), color="white")
font = ImageFont.truetype("arial.ttf", 30, encoding="utf-8")
bigfont = ImageFont.truetype("arial.ttf", 50, encoding="utf-8")
draw = ImageDraw.Draw(img)
draw.text((50, 50), f"A {lifetime}-Year Lifetime in Weeks", font=bigfont, fill="black")
draw.text(
    (130, 150), f'Birthday: {birthday.strftime("%d.%m.%Y")}', font=font, fill="black",
)
y = 200
x = 130 + 15 * round((birthday - datetime(birthday.year, 1, 1)).days / 7)
while birthday < deathday:
    if not birthday.weekday():  # check for mondays
        draw.rectangle(
            (x, y, x + 8, y + 8),
            fill="black" if today < birthday else (150, 0, 0),  # dark red
        )
        x += 15
    newday = birthday + timedelta(days=1)
    if newday.year != birthday.year:
        x = 130
        y += 15
        if not (newday.year - 1) % 5:
            draw.text((50, y), f"{birthday.year}", font=font, fill="black")
            y += 5
    birthday = newday
draw.text(
    (130, y + 35),
    f'Deathday: {deathday.strftime("%d.%m.%Y")}',
    font=font,
    fill="black",
)
img.save("lifetime.png")
img.show()
