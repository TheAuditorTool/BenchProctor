# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest31455():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
