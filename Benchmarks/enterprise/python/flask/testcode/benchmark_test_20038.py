# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20038():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
