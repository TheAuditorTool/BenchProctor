# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest12774():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
