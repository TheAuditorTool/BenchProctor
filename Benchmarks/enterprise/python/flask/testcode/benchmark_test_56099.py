# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest56099():
    multipart_value = request.form.get('multipart_field', '')
    data = default_blank(multipart_value)
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
