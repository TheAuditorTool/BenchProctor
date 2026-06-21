# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest69586():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(graphql_var).encode())
    return jsonify({'length': len(ciphertext)}), 200
