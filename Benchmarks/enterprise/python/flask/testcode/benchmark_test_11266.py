# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11266():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
