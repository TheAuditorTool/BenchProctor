# SPDX-License-Identifier: Apache-2.0
import random
import json
from flask import request, jsonify


def BenchmarkTest58481():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
