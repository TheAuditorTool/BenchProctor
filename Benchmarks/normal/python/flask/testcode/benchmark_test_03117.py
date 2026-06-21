# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest03117():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
