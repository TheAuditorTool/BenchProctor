# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import socket


@dataclass
class FormData:
    payload: str

def BenchmarkTest01277(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
