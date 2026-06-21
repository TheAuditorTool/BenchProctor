# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51496():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
