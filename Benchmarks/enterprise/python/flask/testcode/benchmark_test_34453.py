# SPDX-License-Identifier: Apache-2.0
import re
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest34453():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
