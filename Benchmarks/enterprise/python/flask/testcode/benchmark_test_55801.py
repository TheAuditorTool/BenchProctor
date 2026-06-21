# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import socket


def BenchmarkTest55801():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
