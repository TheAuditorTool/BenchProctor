# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest76341():
    referer_value = request.headers.get('Referer', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', referer_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = referer_value
    eval(str(processed))
    return jsonify({"result": "success"})
