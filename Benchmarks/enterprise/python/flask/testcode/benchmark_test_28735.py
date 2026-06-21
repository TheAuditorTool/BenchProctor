# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28735():
    user_id = request.args.get('id', '')
    return jsonify({'error': str(user_id), 'stack': repr(locals())}), 500
