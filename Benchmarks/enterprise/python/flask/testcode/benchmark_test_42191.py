# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest42191():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
