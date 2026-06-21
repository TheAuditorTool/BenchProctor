# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest75759():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
