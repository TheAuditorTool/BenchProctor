# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest10732():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
