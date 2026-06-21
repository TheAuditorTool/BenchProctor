# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09985():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
