# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30092():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % (forwarded_ip,)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
