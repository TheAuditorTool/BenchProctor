# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80263():
    host_value = request.headers.get('Host', '')
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(host_value)}
