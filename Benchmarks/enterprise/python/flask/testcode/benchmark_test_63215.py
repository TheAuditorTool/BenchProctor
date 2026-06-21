# SPDX-License-Identifier: Apache-2.0
import random
import json
from flask import request, jsonify


def BenchmarkTest63215():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
