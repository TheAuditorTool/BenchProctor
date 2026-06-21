# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27100():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
