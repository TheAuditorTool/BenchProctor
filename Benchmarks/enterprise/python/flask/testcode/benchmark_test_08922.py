# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08922():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
