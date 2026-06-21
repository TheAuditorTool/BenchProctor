# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest70221():
    raw_body = request.get_data(as_text=True)
    data = ensure_str(raw_body)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
