# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest76436():
    field_value = request.form.get('field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', field_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = field_value
    eval(str(processed))
    return jsonify({"result": "success"})
