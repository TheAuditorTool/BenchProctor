# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20115():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
