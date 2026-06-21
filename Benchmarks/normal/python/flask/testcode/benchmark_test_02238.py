# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02238():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return str(processed), 200, {'Content-Type': 'text/html'}
