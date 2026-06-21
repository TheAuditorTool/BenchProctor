# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64220():
    multipart_value = request.form.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
