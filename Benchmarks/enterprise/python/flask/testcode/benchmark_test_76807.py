# SPDX-License-Identifier: Apache-2.0
import hashlib
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db, auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest76807():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
