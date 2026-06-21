# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest32142():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '{}'.format(json_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
