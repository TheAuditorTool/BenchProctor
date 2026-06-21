# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38441():
    user_id = request.args.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
