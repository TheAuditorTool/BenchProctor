# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest78451():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = RequestPayload(secret_value).value
    db.connect(host='localhost', user='app', password=data)
    return jsonify({"result": "success"})
