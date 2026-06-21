# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest11859():
    field_value = request.form.get('field', '')
    db.execute('UPDATE users SET name = ?', (str(field_value),))
    return jsonify({"result": "success"})
