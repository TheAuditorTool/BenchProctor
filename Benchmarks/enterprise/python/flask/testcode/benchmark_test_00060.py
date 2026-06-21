# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import json
from flask import jsonify
import os
from app_runtime import db


def BenchmarkTest00060():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return jsonify({"result": "success"})
