# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest59519():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    reader = make_reader(yaml_value)
    data = reader()
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
