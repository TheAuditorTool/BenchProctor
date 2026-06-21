# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest50678():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
