# SPDX-License-Identifier: Apache-2.0
import secrets
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest46223(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
