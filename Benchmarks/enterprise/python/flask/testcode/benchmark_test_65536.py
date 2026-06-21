# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest65536():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
