# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest44822():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    return str(data), 200, {'Content-Type': 'text/html'}
