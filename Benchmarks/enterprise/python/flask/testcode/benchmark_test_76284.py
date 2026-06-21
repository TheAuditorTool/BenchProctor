# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76284():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
