# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45478():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
