# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest41675():
    upload_name = request.files['upload'].filename
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(upload_name).encode())
    return jsonify({'length': len(ciphertext)}), 200
