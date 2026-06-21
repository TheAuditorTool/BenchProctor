# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest12490():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    requests.get(str(data))
    return jsonify({"result": "success"})
