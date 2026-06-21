# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02472():
    user_id = request.args.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
