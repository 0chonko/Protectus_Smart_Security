from flask import (
    Blueprint, render_template, Response
)

from protectus.auth import login_required
import cv2

# -1 takes default. To specify a specific video device take /dev/video* where * is the number.
feed = cv2.VideoCapture(0)

bp = Blueprint('video', __name__)


@bp.route('/video')
@login_required
def video():
    return render_template("video.html")


def generate(feed):
    while True:
        flag, image = feed.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@bp.route('/video_feed')
@login_required
def video_feed():
    global feed
    return Response(generate(feed),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
