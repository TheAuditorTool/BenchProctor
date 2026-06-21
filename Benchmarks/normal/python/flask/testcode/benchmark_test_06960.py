# SPDX-License-Identifier: Apache-2.0
import random
import base64
from flask import request, jsonify


def BenchmarkTest06960():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
