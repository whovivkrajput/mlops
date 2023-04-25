from flask import Flask
from victor_force.logger import logging

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    logging.info("We are testing out logging file")
    return "Hello World..!!!"

if __name__ == "__main__":
    app.run(debug=True)
