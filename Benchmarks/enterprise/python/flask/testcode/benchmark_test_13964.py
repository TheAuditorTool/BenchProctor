# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest13964():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = FormData(payload=json_value).payload
    return str(data), 200, {'Content-Type': 'text/html'}
