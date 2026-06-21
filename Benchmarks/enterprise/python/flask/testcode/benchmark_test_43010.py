# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest43010():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    session['user'] = str(data)
    return jsonify({"result": "success"})
