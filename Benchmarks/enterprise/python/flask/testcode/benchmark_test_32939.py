# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32939():
    host_value = request.headers.get('Host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
