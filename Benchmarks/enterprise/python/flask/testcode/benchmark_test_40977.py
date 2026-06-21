# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest40977():
    ua_value = request.headers.get('User-Agent', '')
    random.seed(int(ua_value) if str(ua_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
