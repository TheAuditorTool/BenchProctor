# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03415():
    referer_value = request.headers.get('Referer', '')
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(referer_value)}
