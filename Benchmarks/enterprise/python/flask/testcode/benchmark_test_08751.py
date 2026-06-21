# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest08751():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
