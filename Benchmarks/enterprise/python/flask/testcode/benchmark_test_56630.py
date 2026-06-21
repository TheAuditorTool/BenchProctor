# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56630():
    multipart_value = request.form.get('multipart_field', '')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(multipart_value)}
