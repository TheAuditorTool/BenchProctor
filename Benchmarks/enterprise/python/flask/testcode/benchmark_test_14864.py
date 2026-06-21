# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest14864():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
