# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07414():
    multipart_value = request.form.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
