# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest32944():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    return jsonify({'error': 'An internal error occurred'}), 500
