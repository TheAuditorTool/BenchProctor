# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13336():
    user_id = request.args.get('id', '')
    return jsonify({'error': 'An internal error occurred'}), 500
