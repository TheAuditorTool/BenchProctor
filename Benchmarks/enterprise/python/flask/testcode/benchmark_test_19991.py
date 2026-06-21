# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import json
from flask import request, jsonify


def BenchmarkTest19991():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
