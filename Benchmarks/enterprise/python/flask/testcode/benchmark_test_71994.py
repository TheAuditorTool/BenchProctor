# SPDX-License-Identifier: Apache-2.0
import random
import json
from flask import request, jsonify


def BenchmarkTest71994():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
