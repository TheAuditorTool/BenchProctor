# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37897():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
