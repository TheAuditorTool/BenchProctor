# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest81460():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
