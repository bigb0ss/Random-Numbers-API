from flask import Flask,jsonify
from flask_cors import CORS

import numpy as np
app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
	num = np.random.randint(100)
	d={"number":num}
	return jsonify(d)


app.run(port='107')
