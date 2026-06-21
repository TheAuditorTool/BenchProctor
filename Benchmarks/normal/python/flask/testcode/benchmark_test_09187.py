# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09187():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
