# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest57412():
    header_value = request.headers.get('X-Custom-Header', '')
    prefix = ''
    data = prefix + str(header_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
