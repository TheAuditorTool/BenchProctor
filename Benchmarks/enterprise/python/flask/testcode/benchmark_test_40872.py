# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest40872():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
