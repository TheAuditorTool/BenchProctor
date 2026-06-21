# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest68405():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return jsonify({"result": "success"})
