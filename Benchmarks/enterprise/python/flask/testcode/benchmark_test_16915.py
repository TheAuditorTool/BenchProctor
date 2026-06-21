# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16915():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
