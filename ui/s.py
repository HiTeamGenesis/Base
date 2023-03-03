import cv2
import time
from flask import Flask, Response

app = Flask(__name__)

camera = cv2.VideoCapture(0)  # 0 is the ID of the default camera

def generate_frames():
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()
        if not success:
            break
        else:

            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame in the byte format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.001)

@app.route('/')
def index():
    # Video streaming home page
    return """z
        <html>
            <head>
                <title>Live Streaming</title>
            </head>
            <body>
                <h1>Live Streaming</h1>
                <img src="/video_feed">
            </body>
        </html>
    """

@app.route('/video_feed')
def video_feed():
    # Video streaming route. Put this in the src attribute of an img tag
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
