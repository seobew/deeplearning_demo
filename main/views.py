from django.conf import settings
from django.shortcuts import render
import base64
from io import StringIO
import PIL.Image
from PIL import Image
from base64 import decodebytes
import re
import os
import io
from subprocess import call

# Create your views here.

def main(request):
    # cmd = 'python ./tensorflow_part/pix2pix.py --mode test --output_dir facades_test --input_dir facades/val --checkpoint facades_train'
    # cmd = 'python ./tensorflow_part/pix2pix.py --mode test --output_dir chicken_test --input_dir chicken/val --checkpoint chicken_train'
    # cmd = 'python ./tensorflow_part/pix2pix.py --mode test --output_dir chicken_test --input_dir chicken/val --checkpoint chicken_train'
    # os.system(cmd)
    flag = 0

    if request.POST:
        file = request.FILES['test_image'].file

        im = Image.open(file)
        im.save("static/img/temp.png", "PNG")
        im2 = Image.open(open("/Users/kimiseob/Documents/workspace/django/chicken_pix2pix/static/img/test.jpg", 'rb'))

        new_width = 512
        new_height = 256
        new_im = Image.new('RGB', (new_width, new_height))

        x_offset = 0
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]
        new_im.paste(im2, (x_offset, 0))
        x_offset += im2.size[0]
        new_im.save('static/input/test.png', 'png')
        flag = 1

        cmd = 'python ./tensorflow_part/pix2pix.py --mode test --output_dir static/output --input_dir static/input --checkpoint chicken_train'
        os.system(cmd)

    if request.is_ajax():
        print('is_ajax')
        print(request.POST)
        save_path = '/Users/kimiseob/Documents/workspace/django/chicken_pix2pix/static/input/'
        completeName = os.path.join(save_path, "test.jpg")
        filename = 'test.png'


    template = 'main.html'
    context = {'flag': flag}

    return render(request, 'main.html', context)
