# SPDX-License-Identifier: Apache-2.0
import re
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest42675():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    values = str(processed).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
