# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest36243():
    raw_body = request.get_data(as_text=True)
    data, _sep, _rest = str(raw_body).partition('\x00')
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
