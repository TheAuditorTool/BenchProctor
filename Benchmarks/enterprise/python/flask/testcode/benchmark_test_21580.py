# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest21580():
    user_id = request.args.get('id', '')
    data = relay_value(user_id)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
