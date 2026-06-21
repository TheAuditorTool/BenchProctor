# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest15984():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
