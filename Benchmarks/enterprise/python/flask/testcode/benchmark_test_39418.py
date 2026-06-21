# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
import sys
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest39418():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = RequestPayload(db_value).value
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
