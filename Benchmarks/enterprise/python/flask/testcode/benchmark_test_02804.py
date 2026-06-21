# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02804():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
