# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import jsonify
import os
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest25494():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return jsonify({"result": "success"})
