# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81267():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
