# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import keyring
from flask import jsonify


def BenchmarkTest73473():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = yaml_value if yaml_value else 'default'
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
