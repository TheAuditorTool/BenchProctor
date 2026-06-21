# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14096():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
