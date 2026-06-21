# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest39954():
    field_value = request.form.get('field', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(field_value).encode())
    return jsonify({'length': len(ciphertext)}), 200
