# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77581():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
