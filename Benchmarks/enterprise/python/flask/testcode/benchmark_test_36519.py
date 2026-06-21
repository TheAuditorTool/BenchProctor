# SPDX-License-Identifier: Apache-2.0
import random
import json
from flask import request, jsonify


def BenchmarkTest36519():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
