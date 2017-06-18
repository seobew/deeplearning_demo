from django.conf import settings
from django.shortcuts import render
import base64
from io import StringIO
import PIL.Image
from PIL import Image
from base64 import decodebytes
import re

# Create your views here.

def main(request):
    if request.is_ajax():
        imgstr = re.search(r'base64,(.*)', request.POST['img']).group(1)
        imgdata = base64.b64decode(imgstr)
        filename = 'test.png'
        with open(filename, 'wb') as f:
            f.write(imgdata)

    return render(request, 'main.html', )