# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest67609():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
