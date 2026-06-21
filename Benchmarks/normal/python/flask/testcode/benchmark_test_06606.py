# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06606():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
