# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08978():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
