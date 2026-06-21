# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest81109():
    user_id = request.args.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', user_id):
        return jsonify({'error': 'forbidden'}), 400
    processed = user_id
    eval(str(processed))
    return jsonify({"result": "success"})
