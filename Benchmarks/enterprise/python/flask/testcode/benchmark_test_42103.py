# SPDX-License-Identifier: Apache-2.0
import random
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest42103():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
