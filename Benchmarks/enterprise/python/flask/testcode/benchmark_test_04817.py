# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import jsonify


def BenchmarkTest04817():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(config_value).encode())
    return jsonify({"result": "success"})
