# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import json
import os


def BenchmarkTest36719():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    try:
        data = json.loads(yaml_value).get('value', yaml_value)
    except (json.JSONDecodeError, AttributeError):
        data = yaml_value
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
