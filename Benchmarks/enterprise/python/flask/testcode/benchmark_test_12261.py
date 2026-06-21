# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import socket


@dataclass
class FormData:
    payload: str

def BenchmarkTest12261():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
