# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64538():
    ua_value = request.headers.get('User-Agent', '')
    data = str(ua_value).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
