# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62521():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
