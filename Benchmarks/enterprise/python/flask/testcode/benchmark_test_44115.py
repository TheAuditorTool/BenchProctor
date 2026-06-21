# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest44115():
    user_id = request.args.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
