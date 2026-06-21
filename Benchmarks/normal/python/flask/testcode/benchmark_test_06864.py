# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest06864():
    origin_value = request.headers.get('Origin', '')
    data = normalise_input(origin_value)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
