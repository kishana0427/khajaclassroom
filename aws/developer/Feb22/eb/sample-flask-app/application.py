from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return """<h1>Hello Flask </h1>
    <p> Welcome to elastic beanstalk </p>
    """

@application.route("/index")
def index():
    return "<p> Index </p>"


if __name__ == "__main__":
    application.debug = True
    application.run()
