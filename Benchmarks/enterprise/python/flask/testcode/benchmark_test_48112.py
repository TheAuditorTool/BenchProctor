# SPDX-License-Identifier: Apache-2.0
import secrets
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest48112():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
