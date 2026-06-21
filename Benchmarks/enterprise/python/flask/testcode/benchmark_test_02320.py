# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import json
from flask import request, jsonify
import os


def BenchmarkTest02320():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return jsonify({"result": "success"})
