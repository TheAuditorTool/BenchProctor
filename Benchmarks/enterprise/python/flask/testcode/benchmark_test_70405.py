# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest70405():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = RequestPayload(comment_value).value
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return jsonify({'record': str(record)}), 200
