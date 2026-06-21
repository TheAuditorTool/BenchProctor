# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest34365():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value}'
    requests.get(str(data))
    return jsonify({"result": "success"})
