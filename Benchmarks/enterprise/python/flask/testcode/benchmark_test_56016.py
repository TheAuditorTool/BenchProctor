# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest56016():
    ua_value = request.headers.get('User-Agent', '')
    data = normalise_input(ua_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
