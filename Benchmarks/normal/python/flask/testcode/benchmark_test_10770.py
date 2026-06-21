# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10770():
    multipart_value = request.form.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
