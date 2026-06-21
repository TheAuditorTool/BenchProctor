# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import socket


@dataclass
class FormData:
    payload: str

def BenchmarkTest11228():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
