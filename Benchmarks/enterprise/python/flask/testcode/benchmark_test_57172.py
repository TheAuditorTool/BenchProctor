# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def relay_value(value):
    return value

def BenchmarkTest57172():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = relay_value(yaml_value)
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
