# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72560():
    referer_value = request.headers.get('Referer', '')
    pending = list(str(referer_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
