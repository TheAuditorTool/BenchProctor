# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest73209():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
