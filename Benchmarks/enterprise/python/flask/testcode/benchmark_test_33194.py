# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest33194():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    random.seed(int(json_value) if str(json_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
