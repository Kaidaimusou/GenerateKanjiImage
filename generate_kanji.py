#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def generate_char_img(char, fontname='C:\Windows\Fonts\msmincho.ttc', size=(64, 64)):
    img = Image.new('L', size, 'white')
    draw = ImageDraw.Draw(img)
    fontsize = int(size[0] * 0.8)
    font = ImageFont.truetype(fontname, fontsize)
    char_displaysize = font.getsize(char)
    offset = tuple((si - sc) // 2 for si, sc in zip(size, char_displaysize))
    assert all(o >= 0 for o in offset)
    draw.text(offset, char, font=font, fill='#000')
    return img

def save_img(img, filepath):
    img.save(filepath, 'png')
    
if __name__ == '__main__':
    import pandas as pd
    dataset = pd.read_table('Joyo_Kanji.txt')
    for kanji in dataset['漢字']:
        path = "joyokanji/" + kanji + ".png"
        if os.path.exists(path):
            continue
        try:
            img = generate_char_img(kanji)
        except AssertionError:
            # 叱でなぜがエラーが出た。個別で生成するとできた。
            print("AssertionError:" + kanji)
            continue
            
        save_img(img, "joyokanji/" + kanji + ".png")
