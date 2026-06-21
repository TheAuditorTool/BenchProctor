# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest27796():
    user_id = request.args.get('id', '')
    data = relay_value(user_id)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
