# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest04479():
    origin_value = request.headers.get('Origin', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', origin_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = origin_value
    eval(str(processed))
    return jsonify({"result": "success"})
