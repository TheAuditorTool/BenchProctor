# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest32626():
    multipart_value = request.form.get('multipart_field', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(multipart_value).encode())
    return jsonify({'length': len(ciphertext)}), 200
