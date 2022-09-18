from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

app=Flask(__name__)

@app.route('/')
def home():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        #logging.info(housing)
        logging.info("Testing the Logging File")
    return "Project has been started"


if __name__=="__main__":
    app.run(debug=True)