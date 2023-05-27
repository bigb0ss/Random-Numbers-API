from flask import Flask,jsonify
from flask_cors import CORS
import requests
from lxml import html
import numpy as np
app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET','POST'])
def root():
	num = np.random.randint(100)
	d={"number":num}
	return jsonify(d)


if __name__ =='__main__':
	app.run(host='0.0.0.0',port=7000)

