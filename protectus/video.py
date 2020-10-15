from flask import (
    Blueprint, render_template, Response
)
from imutils.video import VideoStream
import cv2
import time

bp = Blueprint('video', __name__)

# initialize the output frame
outputFrame = None

vs = VideoStream(usePiCamera=1).start()
# vs = VideoStream(src=0).start()
time.sleep(2.0)


@bp.route('/')
def index():
    return render_template("index.html")


def generate():
    # grab global references to the output frame and lock variables
    global outputFrame

    # loop over frames from the output stream
    while True:
        # check if the output frame is available, otherwise skip
        # the iteration of the loop
        if outputFrame is None:
            continue

        # encode the frame in JPEG format
        (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)

        # ensure the frame was succesfully encoded
        if not flag:
            continue

        # yield the output frame in the byte format
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')


@bp.route('/video_feed')
def video_feed():
    # return the response generated along with the specific media
    # type (mime type)
    return Response(generate(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")
