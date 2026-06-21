# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71532():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
