# -*- coding: utf-8 -*-

from flask import Flask, render_template, Response
#from video_sources import ImageCamera as Camera
from video_sources import PygameCamera as Camera

app = Flask(__name__)

_camera = Camera()

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
