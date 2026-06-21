# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76280():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
