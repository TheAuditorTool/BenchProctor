# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest53386():
    ua_value = request.headers.get('User-Agent', '')
    random.seed(int(ua_value) if str(ua_value).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
