# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest48105():
    field_value = request.form.get('field', '')
    data = ensure_str(field_value)
    processed = data[:64]
    random.seed(int(processed) if str(processed).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
