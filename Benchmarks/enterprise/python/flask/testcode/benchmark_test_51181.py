# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51181():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
