# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09812():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
