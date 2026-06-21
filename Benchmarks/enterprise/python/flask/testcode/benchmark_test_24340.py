# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest24340():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
