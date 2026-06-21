# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17966():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
