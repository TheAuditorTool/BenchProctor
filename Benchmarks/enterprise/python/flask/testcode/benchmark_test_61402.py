# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from urllib.parse import unquote
from flask import request, jsonify
import os


def BenchmarkTest61402():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
