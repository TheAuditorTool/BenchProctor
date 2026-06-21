# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest20532():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
