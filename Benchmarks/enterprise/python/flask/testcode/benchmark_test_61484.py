# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61484():
    user_id = request.args.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
