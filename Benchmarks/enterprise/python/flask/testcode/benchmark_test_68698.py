# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest68698():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
