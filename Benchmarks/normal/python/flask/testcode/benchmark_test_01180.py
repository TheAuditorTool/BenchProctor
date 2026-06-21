# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01180():
    header_value = request.headers.get('X-Custom-Header', '')
    reader = make_reader(header_value)
    data = reader()
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
