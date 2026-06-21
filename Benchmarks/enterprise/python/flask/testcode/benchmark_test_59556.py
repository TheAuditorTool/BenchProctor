# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest59556():
    auth_header = request.headers.get('Authorization', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    requests.get(str(data))
    return jsonify({"result": "success"})
