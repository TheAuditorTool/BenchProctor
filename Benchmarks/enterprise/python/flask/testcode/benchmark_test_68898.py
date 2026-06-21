# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest68898():
    field_value = request.form.get('field', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(field_value),))
    return jsonify({"result": "success"})
