# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import base64
from flask import jsonify
import os
from app_runtime import db


def BenchmarkTest01914():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
