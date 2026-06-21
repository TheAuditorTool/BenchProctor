# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import json
from flask import jsonify


def BenchmarkTest05566():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = json.loads(file_value).get('value', '')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
