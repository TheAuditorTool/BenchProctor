# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56194():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
