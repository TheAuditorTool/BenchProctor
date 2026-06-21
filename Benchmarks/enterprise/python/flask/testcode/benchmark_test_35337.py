# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35337():
    auth_header = request.headers.get('Authorization', '')
    pending = list(str(auth_header).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
