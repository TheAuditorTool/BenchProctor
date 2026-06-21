# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import requests
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest03663():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
