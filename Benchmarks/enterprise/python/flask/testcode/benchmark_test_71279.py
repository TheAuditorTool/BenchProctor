# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest71279():
    header_value = request.headers.get('X-Custom-Header', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', header_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = header_value
    eval(str(processed))
    return jsonify({"result": "success"})
