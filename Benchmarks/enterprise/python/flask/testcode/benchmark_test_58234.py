# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58234():
    ua_value = request.headers.get('User-Agent', '')
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(ua_value)}
