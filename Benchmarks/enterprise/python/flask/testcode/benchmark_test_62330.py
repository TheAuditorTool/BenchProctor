# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest62330():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
