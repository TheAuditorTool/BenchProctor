# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06412():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
