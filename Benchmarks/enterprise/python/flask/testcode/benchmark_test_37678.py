# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest37678():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
