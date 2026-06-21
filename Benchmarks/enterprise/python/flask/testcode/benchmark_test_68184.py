# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68184():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    pending = list(str(forwarded_ip).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
