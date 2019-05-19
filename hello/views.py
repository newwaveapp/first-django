from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import numpy as np
import threading
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import cv2
import time


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_frame2(self):
        ret, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

cam = VideoCamera()


def gen(camera):

    while True:
        frame = camera.get_frame2()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        #time.sleep(1)


@gzip.gzip_page
def stream2(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass

def stream(request):
    template = loader.get_template('hello/stream.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('hello/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))
