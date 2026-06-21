# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest06960():
    field_value = request.form.get('field', '')
    data = normalise_input(field_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
