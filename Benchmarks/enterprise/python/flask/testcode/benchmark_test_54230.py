# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db, auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest54230():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    auth_check('user', data)
    return jsonify({"result": "success"})
