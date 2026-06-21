# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import socket


def BenchmarkTest23780():
    raw_body = request.get_data(as_text=True)
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
