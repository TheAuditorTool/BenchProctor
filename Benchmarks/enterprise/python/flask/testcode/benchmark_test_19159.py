# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19159():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
