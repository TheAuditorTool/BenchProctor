# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32772():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
