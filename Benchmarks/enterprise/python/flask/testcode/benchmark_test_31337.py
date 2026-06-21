# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest31337():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    ctx = RequestContext(yaml_value)
    data = ctx.payload
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
