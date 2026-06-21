# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14129():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = multipart_value
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
