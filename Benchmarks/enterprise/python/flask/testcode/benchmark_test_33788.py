# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest33788():
    ua_value = request.headers.get('User-Agent', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', ua_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = ua_value
    eval(str(processed))
    return jsonify({"result": "success"})
