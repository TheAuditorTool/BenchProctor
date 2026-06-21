# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72590():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
