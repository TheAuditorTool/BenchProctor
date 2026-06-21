# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def BenchmarkTest37376():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = ' '.join(str(yaml_value).split())
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
