# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest13042():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return jsonify({"result": "success"})
