# SPDX-License-Identifier: Apache-2.0
import re
from dataclasses import dataclass
from flask import jsonify
import unicodedata
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest04079():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
