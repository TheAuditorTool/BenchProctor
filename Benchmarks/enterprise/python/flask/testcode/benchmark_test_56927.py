# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest56927():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    prefix = ''
    data = prefix + str(json_value)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
