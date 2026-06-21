# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest35899():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
