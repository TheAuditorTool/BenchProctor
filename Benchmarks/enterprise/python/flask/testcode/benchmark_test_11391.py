# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest11391():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
