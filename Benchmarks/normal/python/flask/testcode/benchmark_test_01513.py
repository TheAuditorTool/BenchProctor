# SPDX-License-Identifier: Apache-2.0
import re
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest01513():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    values = str(processed).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
