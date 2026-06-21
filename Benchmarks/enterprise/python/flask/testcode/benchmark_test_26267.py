# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26267():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
