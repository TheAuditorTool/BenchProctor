# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest49246():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
