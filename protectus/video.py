from flask import (
    Blueprint, render_template, Response
)

import cv2
rumps

video = cv2.VideoCapture(-1)

bp = Blueprint('video', __name__)


@bp.route('/')
def index():
    return render_template("index.html")


def gen(video):
    while True:
        flag, image = video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@bp.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
