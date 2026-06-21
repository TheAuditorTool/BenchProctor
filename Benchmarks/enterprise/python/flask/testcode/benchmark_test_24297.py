# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest24297():
    multipart_value = request.form.get('multipart_field', '')
    data = ensure_str(multipart_value)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return jsonify({"result": "success"})
