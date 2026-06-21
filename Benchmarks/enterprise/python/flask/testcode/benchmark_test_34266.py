# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest34266():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
