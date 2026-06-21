# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import socket


def BenchmarkTest59143():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
