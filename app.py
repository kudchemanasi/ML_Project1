from flask import Flask
from housing.exception import HousingException
from housing.logger import logging
import sys

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        raise HousingException(e,sys) from e
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."


if __name__ == '__main__':
    app.run(debug=True)

