# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest00585():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
