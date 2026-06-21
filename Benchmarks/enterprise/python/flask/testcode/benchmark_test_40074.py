# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest40074():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
