# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest50910():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
