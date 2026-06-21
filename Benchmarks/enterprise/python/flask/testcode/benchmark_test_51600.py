# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import json


def BenchmarkTest51600():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    try:
        data = json.loads(file_value).get('value', file_value)
    except (json.JSONDecodeError, AttributeError):
        data = file_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
