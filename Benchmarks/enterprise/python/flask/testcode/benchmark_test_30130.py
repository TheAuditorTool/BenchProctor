# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30130():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
