# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import yaml
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02696():
    secret_value = 'app_display_name'
    reader = make_reader(secret_value)
    data = reader()
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
