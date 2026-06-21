# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34318():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
