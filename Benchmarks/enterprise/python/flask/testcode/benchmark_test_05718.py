# SPDX-License-Identifier: Apache-2.0
import secrets
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest05718():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
