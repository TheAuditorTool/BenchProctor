# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest43226():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
