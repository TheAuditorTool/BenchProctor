# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def BenchmarkTest10589():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(yaml_value)
    data = collected
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
