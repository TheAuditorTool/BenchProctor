# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest05267():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
