# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest32011():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
