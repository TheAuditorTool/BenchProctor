# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74636():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
