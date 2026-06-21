# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest49920():
    user_id = request.args.get('id', '')
    _resp = requests.get(str(user_id))
    exec(_resp.text)
    return jsonify({"result": "success"})
