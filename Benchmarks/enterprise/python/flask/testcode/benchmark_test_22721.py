# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest22721():
    field_value = request.form.get('field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', field_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = field_value
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return jsonify({'lookup': arr[idx]}), 200
