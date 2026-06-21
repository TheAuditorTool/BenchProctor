# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02592():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
