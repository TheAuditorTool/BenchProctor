# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os
from types import SimpleNamespace


def BenchmarkTest01994():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    ns = SimpleNamespace(payload=config_value)
    data = getattr(ns, 'payload')
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
