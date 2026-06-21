# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest02741(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
