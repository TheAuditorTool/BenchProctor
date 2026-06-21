# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest49400():
    multipart_value = request.form.get('multipart_field', '')
    data = to_text(multipart_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
