# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest56850():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
