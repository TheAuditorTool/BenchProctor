# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56766():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
