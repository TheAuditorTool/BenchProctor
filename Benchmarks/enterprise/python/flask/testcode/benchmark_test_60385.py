# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest60385():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
