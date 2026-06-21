# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest27400():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = FormData(payload=secret_value).payload
    db.connect(host='localhost', user='app', password=data)
    return jsonify({"result": "success"})
