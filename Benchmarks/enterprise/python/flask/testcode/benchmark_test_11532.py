# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest11532():
    host_value = request.headers.get('Host', '')
    data = '%s' % (host_value,)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
