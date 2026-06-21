# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest11670():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
