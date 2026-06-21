# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import socket


@dataclass
class FormData:
    payload: str

def BenchmarkTest07604():
    host_value = request.headers.get('Host', '')
    data = FormData(payload=host_value).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
