# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest04943():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return jsonify({"result": "success"})
