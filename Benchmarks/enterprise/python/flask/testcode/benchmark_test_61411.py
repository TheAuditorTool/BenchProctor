# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest61411():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
