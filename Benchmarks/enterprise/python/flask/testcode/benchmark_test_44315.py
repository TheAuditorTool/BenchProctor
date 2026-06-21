# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def BenchmarkTest44315():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(yaml_value).encode())
    return jsonify({"result": "success"})
