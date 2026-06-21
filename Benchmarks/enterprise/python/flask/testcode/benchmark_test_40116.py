# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40116():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
