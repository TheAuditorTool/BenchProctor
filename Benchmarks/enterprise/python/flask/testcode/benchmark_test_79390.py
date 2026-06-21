# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest79390():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
