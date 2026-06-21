# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest40407():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
