# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest78713():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
