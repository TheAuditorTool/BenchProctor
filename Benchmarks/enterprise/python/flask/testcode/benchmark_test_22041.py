# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest22041():
    raw_body = request.get_data(as_text=True)
    random.seed(int(raw_body) if str(raw_body).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
