# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53402():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
