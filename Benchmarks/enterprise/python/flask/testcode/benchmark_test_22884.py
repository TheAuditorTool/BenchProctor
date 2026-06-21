# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22884():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
