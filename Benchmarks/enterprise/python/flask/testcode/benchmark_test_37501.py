# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest37501():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
