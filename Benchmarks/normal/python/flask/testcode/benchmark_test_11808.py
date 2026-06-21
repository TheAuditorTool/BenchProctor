# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest11808():
    header_value = request.headers.get('X-Custom-Header', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', header_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = header_value
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return jsonify({'lookup': arr[idx]}), 200
