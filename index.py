from flask import Flask,jsonify
from flask_cors import CORS

import numpy as np
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def root():
	num = np.random.randint(100)
	d={"number":num}
	return jsonify(d)


if __name__ =='__main__':
	app.run()

