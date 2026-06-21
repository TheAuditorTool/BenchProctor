# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37140():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ' '.join(str(json_value).split())
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
