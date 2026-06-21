# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57076():
    multipart_value = request.form.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
