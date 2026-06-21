# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56017():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
