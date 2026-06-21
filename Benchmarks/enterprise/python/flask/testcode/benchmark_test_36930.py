# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest36930():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
