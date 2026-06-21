# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72062():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
