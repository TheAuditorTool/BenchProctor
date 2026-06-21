# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14208():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ' '.join(str(forwarded_ip).split())
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
