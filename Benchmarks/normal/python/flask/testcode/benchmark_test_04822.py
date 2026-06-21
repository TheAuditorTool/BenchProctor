# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest04822():
    ua_value = request.headers.get('User-Agent', '')
    data = relay_value(ua_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
