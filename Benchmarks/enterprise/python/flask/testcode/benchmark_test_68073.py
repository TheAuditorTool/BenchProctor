# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest68073():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
