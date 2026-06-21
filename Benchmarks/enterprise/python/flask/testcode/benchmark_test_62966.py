# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest62966():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
