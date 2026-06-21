# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16894():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
