# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest09635():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = default_blank(json_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
