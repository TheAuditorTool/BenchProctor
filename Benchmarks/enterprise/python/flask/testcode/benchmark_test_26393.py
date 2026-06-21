# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import json


def BenchmarkTest26393():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    try:
        data = json.loads(prop_value).get('value', prop_value)
    except (json.JSONDecodeError, AttributeError):
        data = prop_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
