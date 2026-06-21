# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest41860():
    upload_name = request.files['upload'].filename
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', upload_name):
        return jsonify({'error': 'forbidden'}), 400
    processed = upload_name
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
