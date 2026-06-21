# SPDX-License-Identifier: Apache-2.0
import secrets
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest08535():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
