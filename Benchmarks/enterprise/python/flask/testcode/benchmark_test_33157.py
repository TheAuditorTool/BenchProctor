# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest33157():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
