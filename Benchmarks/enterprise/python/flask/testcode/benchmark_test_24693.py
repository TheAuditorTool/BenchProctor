# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest24693():
    ua_value = request.headers.get('User-Agent', '')
    random.seed(int(ua_value) if str(ua_value).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
