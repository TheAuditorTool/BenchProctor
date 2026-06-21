# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def BenchmarkTest18279():
    field_value = request.form.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
