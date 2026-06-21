# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest01195():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
