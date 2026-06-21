# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74639():
    ua_value = request.headers.get('User-Agent', '')
    data = str(ua_value).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
