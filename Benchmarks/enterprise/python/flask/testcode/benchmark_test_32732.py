# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32732():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
