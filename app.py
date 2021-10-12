import os
from flask import Flask, jsonify, request
from utils import get_homecanary

app = Flask(__name__)

@app.route('/')
def index():
  return "Current endpoint is /property/septic, more maybe planned in future."

@app.route('/property/septic')
def get_septic():
  if 'address' not in request.args or 'zipcode' not in request.args:
    return "Missing address or zipcode", 400

  address: str = request.args['address']
  zipcode: int = request.args['zipcode']

  # assemble all septic info, currently only homecanary
  homecanary_result = get_homecanary(address=address, zipcode=zipcode)

  return jsonify({
    'homecanary': homecanary_result
  })

# parse the html/json that comes from the repsonse
if __name__ == '__main__':
  app.run(debug=True)
