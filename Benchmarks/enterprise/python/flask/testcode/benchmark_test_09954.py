# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09954():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
