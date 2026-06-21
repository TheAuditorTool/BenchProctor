# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80442():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % (forwarded_ip,)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
