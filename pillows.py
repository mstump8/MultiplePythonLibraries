#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:45:24 2022

@author: morganstump
"""
#This code works with the python package PILLOW
#In this code, I enhance two images
#through brightness, sharpness, and contrast

from PIL import Image, ImageEnhance, ImageFilter


#first image uses Image Filter and Image Enhancements
#second images uses Image Resizing/Crop and Image Enhancements

#spiral image
im = Image.open("space.webp")

width, height = im.size
left = 2
top = height / 5
right = 700
bottom = 3 * height / 3

im = im.crop((left, top, right, bottom))
new = (250, 250)
im = im.resize(new)

#printes for spiral image
print(im.format, im.size, im.mode)
im.filter(ImageFilter.EDGE_ENHANCE()).show()
#im.show() #show original

#3 picture differences for spiral

b = ImageEnhance.Brightness(im)
bb = b.enhance(4.0).show()
s = ImageEnhance.Color(im)
ss = s.enhance(5.0).show()

#flower image
im1 = Image.open("flower1.jpeg")

width, height = im1.size
left = 4
top = height / 2
right = 350
bottom = 2 * height / 2

im1 = im1.crop((left, top, right, bottom))
new = (250, 250)
im1 = im1.resize(new)

#prints for flower image
print(im1.format, im1.size, im1.mode) #show original
im1.show()
e1 = ImageEnhance.Contrast(im1)
e1.enhance(3.5).show("Contrast Flower Image")
s1 = ImageEnhance.Sharpness(im1)
s1.enhance(7.0).show("Sharpness Flower Image")
