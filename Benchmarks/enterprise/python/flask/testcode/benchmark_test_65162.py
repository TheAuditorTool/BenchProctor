# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest65162():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
