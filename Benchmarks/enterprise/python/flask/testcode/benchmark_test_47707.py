# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os


def BenchmarkTest47707():
    user_id = request.args.get('id', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(user_id).encode())
    return jsonify({'length': len(ciphertext)}), 200
