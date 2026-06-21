# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import socket


request_state: dict[str, str] = {}

def BenchmarkTest22476():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        s = socket.create_connection((str(data), 80))
        s.close()
    return jsonify({"result": "success"})
