# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest14031():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = RequestPayload(db_value).value
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
