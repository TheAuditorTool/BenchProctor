# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest58161():
    raw_body = request.get_data(as_text=True)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', raw_body):
        return jsonify({'error': 'forbidden'}), 400
    processed = raw_body
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
