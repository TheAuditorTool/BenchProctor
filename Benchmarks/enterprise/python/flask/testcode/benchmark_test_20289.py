# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import yaml
import json
from flask import jsonify


def BenchmarkTest20289():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = json.loads(yaml_value).get('value', '')
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
