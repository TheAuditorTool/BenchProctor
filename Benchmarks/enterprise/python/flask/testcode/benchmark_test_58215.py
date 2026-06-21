# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58215():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return str(processed), 200, {'Content-Type': 'text/html'}
