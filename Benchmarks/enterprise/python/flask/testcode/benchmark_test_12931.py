# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest12931():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
