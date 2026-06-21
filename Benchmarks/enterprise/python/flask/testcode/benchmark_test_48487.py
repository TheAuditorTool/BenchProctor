# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import json
from flask import jsonify
import os
from app_runtime import db


def BenchmarkTest48487():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    enc_key = os.environ['DATA_ENC_KEY']
    key_expires_at = 1577836800
    if key_expires_at > 0:
        Fernet(enc_key.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})
