# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest12790():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
