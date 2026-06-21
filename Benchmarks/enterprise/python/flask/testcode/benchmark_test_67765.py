# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest67765():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
