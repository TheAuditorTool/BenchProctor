# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from flask import session
from app_runtime import db, auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest75921():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
