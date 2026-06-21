# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest16458():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(prop_value)
    data = collected
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
