# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81039():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
