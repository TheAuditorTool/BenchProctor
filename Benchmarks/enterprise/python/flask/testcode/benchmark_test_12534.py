# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest12534():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
