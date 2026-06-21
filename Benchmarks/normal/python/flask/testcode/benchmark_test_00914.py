# SPDX-License-Identifier: Apache-2.0
import re
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest00914():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return jsonify({'lookup': arr[idx]}), 200
