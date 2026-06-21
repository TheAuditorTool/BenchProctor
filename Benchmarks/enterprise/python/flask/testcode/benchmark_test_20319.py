# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest20319():
    field_value = request.form.get('field', '')
    random.seed(int(field_value) if str(field_value).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
