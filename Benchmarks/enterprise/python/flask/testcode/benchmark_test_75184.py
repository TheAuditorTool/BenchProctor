# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest75184():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
