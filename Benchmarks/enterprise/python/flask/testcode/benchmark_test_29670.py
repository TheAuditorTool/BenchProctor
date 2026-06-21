# SPDX-License-Identifier: Apache-2.0
import secrets
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest29670():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
