from django.conf import settings
from django.shortcuts import render
import base64
from io import StringIO
import PIL.Image
from PIL import Image
from base64 import decodebytes
import re
import os
from subprocess import call

# Create your views here.

def main(request):
    # call(["python ", "./tensorflow_part/tf.py"])
    # cmd = 'python ./tensorflow_part/tf.py'
    # cmd = 'python ./tensorflow_part/pix2pix.py --mode test --output_dir facades_test --input_dir facades/val --checkpoint facades_train'
    cmd = 'python ./tensorflow_part/pix2pix.py --mode test --output_dir chicken_test --input_dir chicken/val --checkpoint chicken_train'
    os.system(cmd)
    if request.is_ajax():
        imgstr = re.search(r'base64,(.*)', request.POST['img']).group(1)
        imgdata = base64.b64decode(imgstr)
        filename = 'test.png'
        with open(filename, 'wb') as f:
            f.write(imgdata)

        # exec(open("./tensorflow_part/tf.py").read())


    return render(request, 'main.html', )