# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest54016():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
