from picamera import PiCamera
import time
from flask import Flask

app = Flask(__name__, "/static")

# Init camera
camera = PiCamera()

@app.route("/", methods=["GET"])
def index():
    return "Bonjour, je suis le projet HexaCamection"


@app.route("/start", methods=["GET"])
def start_camera():
    # Start preview
    camera.start_preview()
    return "done"

@app.route("/capture/<name>", methods=["GET"])
def capture(name):
    camera.capture("./static/img" + name + ".jpg")
    return "done"
    
    


if __name__ == '__main__':
    app.run()
    
