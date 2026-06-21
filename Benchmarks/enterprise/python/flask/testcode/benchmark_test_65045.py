# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest65045():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
