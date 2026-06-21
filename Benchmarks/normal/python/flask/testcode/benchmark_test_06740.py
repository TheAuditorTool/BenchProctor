# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest06740():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return jsonify({'lookup': arr[idx]}), 200
