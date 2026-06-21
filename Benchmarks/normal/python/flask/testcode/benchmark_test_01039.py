# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01039():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
