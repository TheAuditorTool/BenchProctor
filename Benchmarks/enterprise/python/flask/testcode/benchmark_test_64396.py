# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest64396():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
