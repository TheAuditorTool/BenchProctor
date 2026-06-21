# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest01977():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
