# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import yaml
import os
from flask import jsonify


def BenchmarkTest10663():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
