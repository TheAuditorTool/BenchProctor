# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest37456():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = RequestPayload(db_value).value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
