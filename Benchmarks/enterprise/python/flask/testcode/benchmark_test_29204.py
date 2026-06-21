# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import yaml
from flask import jsonify


def BenchmarkTest29204():
    secret_value = 'default_config_label'
    data, _sep, _rest = str(secret_value).partition('\x00')
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
