# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest09648():
    auth_header = request.headers.get('Authorization', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(auth_header)):
        return jsonify({'error': 'invalid input'}), 400
    processed = auth_header
    eval(str(processed))
    return jsonify({"result": "success"})
