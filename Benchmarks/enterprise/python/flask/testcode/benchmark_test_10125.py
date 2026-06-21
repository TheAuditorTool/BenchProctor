# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10125():
    referer_value = request.headers.get('Referer', '')
    return jsonify({'error': str(referer_value), 'stack': repr(locals())}), 500
