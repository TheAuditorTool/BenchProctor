# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest49516():
    field_value = request.form.get('field', '')
    data = relay_value(field_value)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return jsonify({"result": "success"})
