# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31512():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
