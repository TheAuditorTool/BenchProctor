# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os


def BenchmarkTest30565():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = ' '.join(str(prop_value).split())
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
