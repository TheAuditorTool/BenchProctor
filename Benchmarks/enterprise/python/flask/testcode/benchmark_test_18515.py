# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest18515():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
