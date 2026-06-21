# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from flask import session
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest48824():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
