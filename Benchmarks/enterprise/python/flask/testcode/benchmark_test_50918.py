# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50918():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
