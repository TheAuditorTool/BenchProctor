# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest76295():
    user_id = request.args.get('id', '')
    data = default_blank(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
